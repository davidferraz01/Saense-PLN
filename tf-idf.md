---
layout: page
title: TF-IDF
subtitle: Resumos gerados a partir desta técnica
---
## O que é TF-IDF?
O termo **“TF-IDF”** vem do inglês *Term Frequency - Inverse Document Frequency*, ou seja, *Frequência do Termo - Inverso da Frequência dos Documentos*. Representa um valor, obtido através de métodos estatísticos, que tem o intuito de determinar a importância de uma palavra num texto ou em um conjunto de documentos. Tal técnica é muito utilizada na recuperação de informações, na mineração de dados, consultar documentos similares (com cálculo de distância), transformar os textos para alimentar um modelo de aprendizagem de máquina e dentre outras aplicações.

O valor **“TF”** de uma palavra aumenta de maneira proporcional à medida que o seu número de ocorrências aumenta no texto, no entanto, esse valor é equilibrado pelo **“IDF”** que representa o quão rara é a palavra no texto ou documentos. Portanto, temos:

**TF** = *(número de vezes que o termo t aparece no texto) / (número de termos totais no texto)*;

**IDF** = *Log (N/n)*, no qual **N** é o número de documentos ou sentenças no texto, e **n** é o número de documentos em que o termo apareceu.

> **Exemplo**

> - Considere um documento com 100 palavras no qual o termo **“IA”** aparece 5 vezes. Portanto:
  **TF** = 5/100 = 0.05
  
> - Se tivermos 100 documentos ao total e o termo “IA” aparece em 20 desses documentos, logo:
  **IDF** = Log(100/20) = 0.69
  
> - Por fim, o valor TF-IDF do termo “IA” é:
  **TF-IDF** = 0.05 * 0.69 = **0.034**

**OBS.:** É importante ressaltar que quanto maior o **TF-IDF** mais raro será o termo. Consequentemente, quanto menor o valor, mais comum será o mesmo.
