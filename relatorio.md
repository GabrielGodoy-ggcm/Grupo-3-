# Relatório: reconstrução de matrizes (Grupo 3)
Integrantes: 
 Gabriel Godoy Carvalho de Menezes
 Vitor Nunes Silvestre Fernandes Costa
 João Luis de Siqueria Ribeiro

## Chute inicial (média da coluna)
O algoritmo copia a matriz observada e usa a máscara para saber quais valores são conhecidos. Cada buraco é preenchido com a média da sua coluna, calculada só com os valores conhecidos; se a coluna estiver toda escondida, usa-se a média geral. Os valores conhecidos permanecem intactos e o resultado é uma matriz sem NaN, do mesmo tamanho da entrada