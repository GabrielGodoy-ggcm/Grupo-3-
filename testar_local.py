import time
import numpy as numpy
from solucao import principal
# Caminho da pasta banco_publico (ajuste se a sua estiver em outro lugar)
pasta = "pacote_equipe/banco_publico/"
print("matriz | NRMSE  | tempo(s) | formato ok | sem NaN/Inf | conhecidos intactos")
nrmses = []
for i in range(1, 11):
    n = "%02d" % i
    obs = numpy.load(pasta + "observada_" + n + ".npy")
    masc = numpy.load(pasta + "mascara_" + n + ".npy").astype(bool)
    gab = numpy.load(pasta + "gabarito_" + n + ".npy")
    inicio = time.time()
    saida = numpy.array(principal(obs, masc), dtype=float)
    tempo = time.time() - inicio
    formato_ok = saida.shape == obs.shape
    sem_nan = bool(numpy.isfinite(saida).all())
    intactos = bool(numpy.allclose(saida[masc], obs[masc]))
    # erro só nas posições escondidas, dividido pelo desvio padrão do gabarito
    rmse = numpy.sqrt(numpy.mean((saida[~masc] - gab[~masc]) ** 2))
    nrmse = rmse / gab.std()
    nrmses.append(nrmse)
    print(n, "   |", "%.4f" % nrmse, "|", "%.4f" % tempo, "  |", formato_ok, "   |", sem_nan, "      |", intactos)
print("média dos NRMSE:", "%.4f" % numpy.mean(nrmses))
