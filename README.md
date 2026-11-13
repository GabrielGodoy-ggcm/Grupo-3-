# Torneio de reconstrução de matrizes (AVLC / CIN0138)

Equipe: 
 Gabriel Godoy Carvalho de Menezes 
 Vitor Nunes Silvestre Fernandes Costa
 João Luis de Siqueria Ribeiro

## O que tem aqui
- `solucao.py`: o arquivo que vai no zip de entrega (só a função `principal`)
- `testar_local.py`: teste no computador (NÃO vai no zip)
- `relatorio.md`: relatório curto do algoritmo (vai no zip)
- `resultados/baseline.md`: tabela de NRMSE por matriz, anotada a partir do avaliador.
- `versoes/solucao_baseline.py`: cópia de segurança da versão simples (média da coluna). Se uma versão nova der problema, copie este arquivo de volta para `solucao.py`
- `pacote_equipe/`: avaliador dos monitores (extrair o zip aqui). NÃO sobe pro GitHub.

## Regras de ouro
- Só numpy, scipy, math e random. Sem class. Sem seed Funções de apoio só dentro da `principal`
- Sem NaN/Inf, mesmo tamanho da entrada, no máximo 2 s por matriz
- O zip de entrega tem SÓ o `solucao.py` e o relatório
