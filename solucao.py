import numpy as np

def principal(observada, mascara):
    saida = np.array(observada, dtype=float)
    conhecidos = np.array(mascara, dtype=bool) & np.isfinite(saida)
    #parte 1: baseline (chute inicial pela média da coluna)
    if conhecidos.any():
        media_geral = saida[conhecidos].mean()
    else:
        media_geral = 0.0
    soma_por_coluna = np.where(conhecidos, saida, 0.0).sum(axis=0)
    qtd_por_coluna = conhecidos.sum(axis=0)
    media_por_coluna = np.where(qtd_por_coluna > 0, soma_por_coluna / np.maximum(qtd_por_coluna, 1), media_geral)
    chute = np.where(conhecidos, saida, media_por_coluna)
    #parte 2: o loop de SVD (melhora o chute) 
    forma = chute.shape
    linhas = forma[0]
    colunas = forma[1]
    k = min(1, linhas, colunas)
    custo = linhas * colunas * min(linhas, colunas)
    atual = chute.copy()
    if (not conhecidos.all()) and custo <= 5e9:
        n_iter = max(1, min(30, int(2e8 // custo)))
        try:
            for passo in range(n_iter):
                resultado = np.linalg.svd(atual, full_matrices=False)
                u = resultado[0]    #padroes das linhas
                s = resultado[1]    #força de cada padrao (valores singular)
                vt = resultado[2]   #padroes das colunas
                reconstruida = (u[:, :k] * s[:k]) @ vt[:k, :]
                atual = np.where(conhecidos, saida, reconstruida)
        except:
            atual = chute.copy()
    if not np.isfinite(atual).all():
        atual = chute.copy()
    atual = np.nan_to_num(atual, nan=media_geral, posinf=media_geral, neginf=media_geral)
    return atual