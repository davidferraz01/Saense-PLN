---
layout: page
title: Visão Geral
subtitle: Uma breve descrição sobre o projeto
---

### **Objetivo atual**
Esse projeto tem como principal objetivo sumarizar os artigos encontrados na plataforma de divulgação científica [Saense](https://saense.com.br/) visando sua publicação em redes sociais, como o *Instagram*, a fim de disseminar o conhecimento científico tornando-o mais acessível à população. Visto que, é uma das plataformas mais utilizadas pelos Brasileiros, e os textos ali presentes nas publicações apresentam-se de maneira bastante resumida. Portanto, surge a necessidade de sumarizar e postar os textos do portal para que assim um maior público possa ser alcançado.
Ou seja, esse projeto de pesquisa tem como intuito explorar as diferentes técnicas e visões dentro do vasto campo do *Processamento de Linguagens Naturais*. Dessa forma, será implementado dois tipos de algoritmos de sumarização e será realizado a comparação de seus resultados através de diversas métricas de avaliação de qualidade dos resumos. Além disso, esse projeto abre diversas “portas” para trabalhos futuros, seja na continuidade e aprimoramento do mesmo ou seja na contribuição em implementações de outros trabalhos.


### **Ideias futuras**
Com isso em mente, futuramente podemos implementar um algoritmo que identifique as palavras e *sentenças mais importantes do texto* para que seja possível encontrar relações entre os diversos artigos disponíveis no site, agrupando-os. Essa ferramenta pode ser utilizada, juntamente com os algoritmos de sumarização, para auxiliar na criação de um projeto maior, no qual tem como intenção a criação de **Histórias em Quadrinhos** tendo como base os artigos da plataforma Saense para que seja feita a distribuição gratuita em escolas públicas, levando conteúdo científico de forma acessível e de maneira divertida. Sendo assim, as ferramentas aqui projetadas e implementadas tornam-se valiosas para o artista que irá desenvolver os Quadrinhos, pois o mesmo terá uma lista de palavras chaves, postagens relacionadas e o resumo das mesmas, portanto, facilitando o desenvolvimento das *HQ’s*.


### **O que temos atualmente**
Até o momento, temos 5 algoritmos prontos, o "Crawler", dois algoritmos que realizam a sumarização dos textos, por meio de técnicas diferentes, e um último algoritmo que irá auxiliar na criação de uma base de dados para projetos futuros. 
O algoritmo de Crawler é composto por dois scripts em Python, *“handle_page.py"* e *"handle_site.py”*, esses atuam em conjunto para extrair com precisão os textos presentes no site do **Saense**, salvando os mesmos em arquivos *".txt"*, além disso salva informações extras em *".json"* e imagens presentes no artigo que podem ser úteis nas próximas etapas do projeto. Já o Algoritmo de sumarização extrativa, *“summary_tf_idf.py”*, realiza o resumo dos textos extraídos pelo Crawler utilizando uma técnica de sumarização chamada **"TF-IDF"**. Enquanto o segundo algoritmo de sumarização, *“abstractive_summary.ipynb”*, utiliza um **modelo abstrativo** para gerar os resumos. Por fim, o último algoritmo desenvolvido até o momento é o *“create_data_base.py”*, no qual foi baseado numa estratégia adotada pela Google em seu modelo **"Pegasus"** que consiste em gerar grande quantidade de dados para treinar modelos abstrativos.
Seguindo essa linha de raciocínio, o foco atual deste projeto pesquisa está voltado para o algoritmo de sumarização abstrativo, mais especificamente em como podemos realizar a aplicação da base de dados criadas pelo algoritmo, *“create_data_base.py”* já explanado anteriormente, para que seja possível executar um ajuste fino no modelo implementado implicando em uma melhor qualidade dos resumos gerados. Além disso, estamos em continuidade nos estudos voltados à diferentes técnicas de sumarização de texto desde outras técnicas extrativas à abordagens mais complexas utilizando *Word Embeddings* com uma abordagem mais **abstrativa**. Alguns **resultados** de sumarização realizados com os algoritmos podem ser encontrados neste website.


### **Considerações Finais**
Neste Site será documentado o processo, estado atual e os resultados parciais e finais desse estudo em *Processamento de Linguagem Natural (PLN)*. O objetivo é conseguir desenvolver bons algoritmos de sumarização de texto com diferentes abordagens. Dessa forma, teremos explorado e avaliado diferentes técnicas e pontos de vistas na área de *Processamento de Linguagem Natural (PLN)*, expandindo e aprimorando conhecimento dos envolvidos e outras pessoas que se interessam pelo assunto.


<p align="center">
  <embed src="pdfs/relatorio.pdf" type="application/pdf"/>
</p>

