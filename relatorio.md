# Relatório: reconstrução de matrizes (Grupo 3)

Integrantes: 
Gabriel Godoy Carvalho de Menezes
Vitor Nunes Silvestre Fernandes Costa
João Luis de Siqueria Ribeiro

## Algoritmo

O algoritmo tem duas etapas.

**Etapa 1: chute inicial pela média da coluna.**

1. Convertemos a entrada para numpy e a mascara para booleano, só consideramos conhecido o valor que a mascara marca como conhecido e que é um número de verdade (nem NaN, nem infinito);
2. Para cada coluna, somamos os valores conhecidos e dividimos pela quantidade deles, obtendo a média da coluna;
3. Se uma coluna não tem nenhum valor conhecido, usamos a média geral de todos os valores conhecidos (ou 0, se não houver nenhum);
4. Mantemos os valores conhecidos como estavam e colocamos a média da coluna nos buracos;

**Etapa 2: refinamento por SVD iterativa (aproximação de posto 1).** 
Partindo da matriz da etapa 1, repetimos:

1. Calculamos a SVD da matriz atual;
2. Guardamos apenas o maior valor singular (k = 1) e reconstruímos a matriz com esse único padrão;
3. Trocamos somente os buracos pelos valores da reconstrução, os valores conhecidos nunca mudam;

Repetimos até 30 vezes, em matrizes grandes o número de repetições diminui, para respeitar o limite de tempo sem usar relógio, se a SVD der erro ou o resultado tiver NaN ou infinito, voltamos ao chute da etapa 1

## Por que funciona

A média de uma coluna é o valor constante c que minimiza a soma dos erros quadráticos em relação aos valores conhecidos dela, isto é, minimiza a soma de (xi - c)^2. Por isso ela é um bom ponto de partida para o RMSE

Muitas matrizes têm poucos padrões dominantes (posto baixo): suas linhas e colunas se relacionam. A aproximação de posto k obtida pela SVD é a melhor aproximação de posto k no sentido do erro quadrático, e com k = 1 ela descreve a matriz como um perfil de linhas combinado com um perfil de colunas. Ao repetir o processo, os valores estimados para os buracos passam a usar essa relação, em vez de olhar cada coluna isoladamente, escolhemos k = 1 por ser o mais simples
