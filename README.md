# Select-BFPRT em Python

Este projeto implementa o algoritmo **Select-BFPRT** (Mediana de Medianas) em Python para selecionar o z-ésimo maior elemento de um vetor e foi desenvolvido no decorrer da disciplina de **Construção e Análise de Algoritmos** do curso de **Engenharia de Computação da Universidade Federal do Ceará (Campus Sobral)**. Também inclui uma variante com parâmetro ajustável `r`, que define o tamanho dos grupos usados para calcular a mediana nas chamadas recursivas.

## Desenvolvedora
- [Nicole Souza](https://github.com/nicolesouzab) 

## Descrição

O algoritmo recebe uma tripla `(x, y, z)`:

- `x`: um vetor de `y` posições contendo inteiros.
- `y`: o tamanho do vetor.
- `z`: um inteiro tal que `1 ≤ z ≤ y`.

O objetivo é retornar o **z-ésimo maior elemento** do vetor.

Além disso, foi implementada uma versão que aceita o parâmetro `r`, que define o tamanho do grupo utilizado na etapa de mediana. Os valores testados foram: `{3, 5, 7, 9, 11}`.

## Linguagem usada

![Python](https://img.shields.io/badge/Python-14354C?style=flat&logo=python&logoColor=white)

## Resultados

Ao final da execução do script `test.py`, será exibido um relátorio contendo informações sobre os testes realizados do algoritmo Select-BFPRT. Para cada valor de `r ∈ {3, 5, 7, 9, 11}`, utilizando vetores de tamanho fixo com 100.000 elementos, e 200.000 triplas geradas aleatoriamente para cada valor de `r`, representando o tamanho dos grupos utilizados na etapa de mediana.
Onde:

### Relatório de Desempenho

A seguir, os resultados obtidos:

| r  | Tamanho do vetor (y) | Nº de triplas   | Tempo médio por tripla (ms)  |
|----|----------------------|-----------------|------------------------------|
| 3  | 100000               | 200000          | **138.0622**                 |
| 5  | 100000               | 200000          | **76.8702**                  |
| 7  | 100000               | 200000          | **80.2809**                  |
| 9  | 100000               | 200000          | **55.6753**                  |
| 11 | 100000               | 200000          | **51.4857**                  |

### Interpretação

Esse teste serve para avaliar como o desempenho do algoritmo varia conforme o valor de `r`. Em teoria:

- Valores pequenos de `r` (como 3) podem gerar muitos grupos e mais chamadas recursivas;
- Valores grandes (como 11) tornam a ordenação local mais custosa, mas reduzem a profundidade da recursão;
- O valor `r = 5` costuma ser um bom ponto de equilíbrio, sendo o valor usado originalmente no algoritmo BFPRT.

Esses testes ajudam a observar, na prática, **qual valor de `r` oferece o melhor desempenho médio** para os tamanhos de entrada definidos.
