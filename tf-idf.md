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

> **Exemplo**
> Considere um documento com 100 palavras no qual o termo **“IA”** aparece 5 vezes. Portanto:
  **TF** = 5/100 = 0.05
> Se tivermos 100 documentos ao total e o termo “IA” aparece em 20 desses documentos, logo:
  **IDF** = Log(100/20) = 0.69
> Por fim, o valor TF-IDF do termo “IA” é:
  **TF-IDF** = 0.05 * 0.69 = **0.034**

**OBS.:** É importante ressaltar que quanto maior o **TF-IDF** mais raro será o termo. Consequentemente, quanto menor o valor, mais comum será o mesmo.


## Resumos
Veremos agora alguns resumos dos 20 artigos mais lidos do portal [Saense](https://saense.com.br/) gerados a partir dessa técnica. É importante ressaltar que os textos gerados estão com até de 2200 caracteres, visando a postagem dos mesmos no Instagram que impõe tal limite. 

#### [Homossexualidade é genética (e não há “cura”)](https://saense.com.br/2016/08/homossexualidade-e-genetica-e-nao-ha-cura/)
Identificadas regiões nos cromossomos que parecem ser responsáveis pela orientação sexual. Muitas pesquisas em sexualidade começam a demonstrar isso. O DNA é composto por nucleotídeos. Quando apenas um nucleotídeo é trocado na sequência de um gene, chamamos isso de SNP (polimorfismo de nucleotídeo único). Os pesquisadores analisaram os genomas dos 818 indivíduos (gêmeos homossexuais) e também o genoma de mais 90 familiares não-homossexuais desses gêmeos. A análise encontrou SNPs em diversos genes. Isso significa dizer que homossexuais têm alguns genes cuja sequência tem uma única alteração, se comparada aos mesmos genes em heterossexuais. No estudo, as regiões com mais SNPs encontrados estão presentes no cromossomo 8 e no cromossomo X (que é um dos cromossomos sexuais). Dentre os genes com SNPs, muitos estão relacionados ao desenvolvimento neuronal ou participam na neurotransmissão. Isso significa dizer que a orientação sexual parece ser determinada antes do nascimento. Outros dois genes encontrados, AVPR2 e NPBWR1, têm relação com o comportamento e interação social em ratos [6]. Então está tudo explicado? Sequências diferentes nos genes determinam a orientação sexual do indivíduo? Não, nada é tão simples na natureza. Mas a explicação para este fato parece ainda estar na genética, mais precisamente, epigenética. Evidências sugerem que essas diferenças são dependentes da posição do feto no útero e também da quantidade de sangue que o feto recebe da mãe [7]. Curiosamente, mulheres que apresentam a variante de genes homossexuais masculinos não são necessariamente homossexuais e apresentam maior fertilidade. Assim, a alta fecundidade dessas mulheres na população parece “compensar” a taxa de homossexualidade masculina [8]. Os últimos estudos sobre orientação sexual são, no mínimo, interessantes. Além disso, as descobertas em epigenética mostram o quanto o ambiente pode influenciar a orientação sexual do indivíduo, desde antes do nascimento. Do mesmo modo que nascemos com olhos castanhos ou azuis, temos nossa sexualidade intrincada ao nosso DNA. E aqui não me demoro nas questões de preconceitos.

[**Como reduzir o consumo de combustíveis fósseis e impedir o desastre ambiental?**](https://saense.com.br/2016/02/como-reduzir-o-consumo-de-combustiveis-fosseis-e-impedir-o-desastre-ambiental/)
Energia eólica. [1]Economistas norte-americanos realizaram um estudo sobre a questão do uso de combustíveis fósseis e a desejável substituição por fontes alternativas de energia limpa. O trabalho [2] mostrou que o consumo mundial de combustíveis fósseis aumentou 7,5% em petróleo, 24% em carvão, e 20% em gás natural no período de 2005 a 2014. Enquanto isso, as reservas mundiais de petróleo e gás natural, suficientes para o consumo global durante 50 anos, têm permanecido constantes nos últimos 30 anos e as reservas de carvão permitem mais 100 anos de consumo. Os valores constantes de reservas de petróleo e gás natural significam que são descobertas novas reservas, a cada ano, num ritmo mais ou menos igual ao do aumento de consumo. Em outro olhar, a oferta de combustíveis fósseis aumentou consistentemente ao longo do tempo e esses tipos de combustíveis têm mantido vantagem relativa de preço sobre as fontes alternativas de energia limpa (solar, eólica, nuclear, etc.) [2]. Aproximadamente 65% das emissões globais de gases de efeito estufa são gerados pela queima de combustíveis fósseis. Dessas emissões, o carvão é responsável por 45%, o petróleo por 35%, e gás natural por 20%. Para reduzir as emissões de dióxido de carbono (CO2) de forma a mitigar a possibilidade de mudança perturbadora do clima, parece haver apenas duas opções possíveis. Uma é encontrar maneiras de capturar o CO2 do ar (através da expansão das florestas, por exemplo). A outra é reduzir o consumo de combustíveis fósseis de forma drástica [2]. Observa-se que pouco esforço prático tem sido feito pelos países para enfrentar o problema. O fato observado nos últimos anos é que não está ocorrendo diminuição de oferta de combustíveis fósseis a baixo custo, nem os avanços na produção de energia limpa têm levado à substituição dos combustíveis fósseis de forma notável. Assim, a perspectiva é assustadora!
