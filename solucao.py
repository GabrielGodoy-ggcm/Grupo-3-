import numpy as numpy
def principal(observada, mascara):
#converte tudo pra array de numpy, pra não dar problema se chegar como lista
#a mascara vira booleana: True = valor conhecido, False = buraco
    saida = numpy.array(observada, dtype=float)
#só conta como "conhecido" se a máscara diz que é E o número é de verdade(não é NaN nem infinito). Assim nenhuma média é contaminada por valor ruim
    conhecidos = numpy.array(mascara, dtype=bool) & numpy.isfinite(saida)
#media de todos os valores que a gente SABE(Vai servir de plano B)
#caso alguma coluna esteja toda escondida
    if conhecidos.any():
        media_geral = saida[conhecidos].mean()
    else:
        media_geral = 0.0
#soma de cada coluna olhando só os valores conhecidos, (os buracos viram 0 aqui, então não atrapalham a soma)
    soma_por_coluna = numpy.where(conhecidos, saida, 0.0).sum(axis=0)
#quantos valores conhecidos cada coluna tem
    qtd_por_coluna = conhecidos.sum(axis=0)
#media de cada coluna. Se a coluna não tem nenhum valor conhecido, usa a media geral (o numpy.maximum só evita dividir por zero)
    media_por_coluna = numpy.where(qtd_por_coluna > 0, soma_por_coluna / numpy.maximum(qtd_por_coluna, 1), media_geral)
#onde era conhecido, mantém o valor original. Onde era buraco, coloca a média da coluna daquela posição
    saida = numpy.where(conhecidos, saida, media_por_coluna)
#segurança extra: pelo que fizemos acima não deveria sobrar NaN nem infinito, mas se sobrar, troca pela média geral
    saida = numpy.nan_to_num(saida, nan=media_geral, posinf=media_geral, neginf=media_geral)
    return saida