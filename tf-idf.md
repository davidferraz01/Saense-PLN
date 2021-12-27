---
layout: page
title: TF-IDF
subtitle: Resumos gerados a partir desta técnica
---
## O que é TF-IDF?
O termo **“TF-IDF”** vem do inglês *Term Frequency - Inverse Document Frequency*, ou seja, *Frequência do Termo - Inverso da Frequência dos Documentos*. Representa um valor, obtido através de métodos estatísticos, que tem o intuito de determinar a importância de uma palavra num texto ou em um conjunto de documentos. Tal técnica é muito utilizada na recuperação de informações, na mineração de dados, consultar documentos similares (com cálculo de distância), transformar os textos para alimentar um modelo de aprendizagem de máquina e dentre outras aplicações.

O valor **“TF”** de uma palavra aumenta de maneira proporcional à medida que o seu número de ocorrências aumenta no texto, no entanto, esse valor é equilibrado pelo **“IDF”** que representa o quão rara é a palavra no texto ou documentos. Portanto, temos:

**TF** = *(número de vezes que o termo t aparece no texto) / (número de termos totais no texto)*
**IDF** = *Log (N/n)*, no qual **N** é o número de documentos ou sentenças no texto, e **n** é o número de documentos em que o termo apareceu

#### Exemplo:
Considere um documento com 100 palavras no qual o termo **“IA”** aparece 5 vezes. Portanto:
**TF** = 5/100 = 0.05

Se tivermos 100 documentos ao total e o termo “IA” aparece em 20 desses documentos, logo:
**IDF** = Log(100/20) = 0.69

Por fim, o valor TF-IDF do termo “IA” é:
**TF-IDF** = 0.05 * 0.69 = **0.034**

É importante ressaltar que quanto maior o **TF-IDF** mais raro será o termo. Consequentemente, quanto menor o valor, mais comum será o mesmo.


## Resumos
Veremos agora alguns resumos dos 20 artigos mais lidos do portal [Saense](https://saense.com.br/) gerados a partir dessa técnica.

### [Homossexualidade é genética (e não há “cura”)](https://saense.com.br/2016/08/homossexualidade-e-genetica-e-nao-ha-cura/)
Identificadas regiões nos cromossomos que parecem ser responsáveis pela orientação sexual. Muitas pesquisas em sexualidade começam a demonstrar isso. O DNA é composto por nucleotídeos. Quando apenas um nucleotídeo é trocado na sequência de um gene, chamamos isso de SNP (polimorfismo de nucleotídeo único). Os pesquisadores analisaram os genomas dos 818 indivíduos (gêmeos homossexuais) e também o genoma de mais 90 familiares não-homossexuais desses gêmeos. A análise encontrou SNPs em diversos genes. Isso significa dizer que homossexuais têm alguns genes cuja sequência tem uma única alteração, se comparada aos mesmos genes em heterossexuais. No estudo, as regiões com mais SNPs encontrados estão presentes no cromossomo 8 e no cromossomo X (que é um dos cromossomos sexuais). Dentre os genes com SNPs, muitos estão relacionados ao desenvolvimento neuronal ou participam na neurotransmissão. Isso significa dizer que a orientação sexual parece ser determinada antes do nascimento. Outros dois genes encontrados, AVPR2 e NPBWR1, têm relação com o comportamento e interação social em ratos [6]. Então está tudo explicado? Sequências diferentes nos genes determinam a orientação sexual do indivíduo? Não, nada é tão simples na natureza. Mas a explicação para este fato parece ainda estar na genética, mais precisamente, epigenética. Evidências sugerem que essas diferenças são dependentes da posição do feto no útero e também da quantidade de sangue que o feto recebe da mãe [7]. Curiosamente, mulheres que apresentam a variante de genes homossexuais masculinos não são necessariamente homossexuais e apresentam maior fertilidade. Assim, a alta fecundidade dessas mulheres na população parece “compensar” a taxa de homossexualidade masculina [8]. Os últimos estudos sobre orientação sexual são, no mínimo, interessantes. Além disso, as descobertas em epigenética mostram o quanto o ambiente pode influenciar a orientação sexual do indivíduo, desde antes do nascimento. Do mesmo modo que nascemos com olhos castanhos ou azuis, temos nossa sexualidade intrincada ao nosso DNA. E aqui não me demoro nas questões de preconceitos.
