# Relatório: reconstrução de matrizes (Grupo 3)
Integrantes: 
 Gabriel Godoy Carvalho de Menezes
 Vitor Nunes Silvestre Fernandes Costa
 João Luis de Siqueria Ribeiro

## Problema
Cada matriz chega com valores escondidos. A função principal(observada, mascara) recebe a matriz visível e uma máscara que indica quais posições são conhecidas, e devolve a matriz completa, com o mesmo tamanho. O erro é medido só nas posições escondidas, pelo NRMSE (RMSE dividido pelo desvio padrão dos valores reais).

## Algoritmo
O algoritmo copia a matriz observada e usa a máscara para saber quais valores são conhecidos, cada valor escondido é preenchido com a média da sua coluna, calculada só com os valores conhecidos, se a coluna estiver toda escondida, usa-se a média geral dos valores conhecidos. Os valores conhecidos permanecem intactos, e o resultado é uma matriz do mesmo tamanho da entrada, sem NaN e sem infinitos, a média da coluna é o valor constante que minimiza o erro quadrático em relação aos valores conhecidos dela, por isso é um chute inicial simples e coerente com a métrica (RMSE).

## Por que a média
A média de uma coluna é o valor constante c que minimiza a soma dos erros quadráticos em relação aos valores conhecidos dela, isto é, minimiza a soma de (xi - c)^2. Como o RMSE é a raiz da média dos erros ao quadrado, a média é o melhor chute constante quando os valores escondidos se parecem com os conhecidos e não usamos nenhuma outra informação sobre a matriz.

