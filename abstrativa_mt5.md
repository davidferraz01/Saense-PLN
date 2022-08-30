---
layout: page
title: Algoritmo mT5
subtitle: Resultados obtidos através desse algoritmo
---
## Sumarização Abstrativa com mT5?
Levando em consideração os problemas encontrados com o algoritmo do [Google Pegasus](https://0xdferraz.github.io/Saense-PLN/abstrativa_pegasus/) citados anteriormente, iniciou-se a busca por outro modelo pré-treinado abstrativo que não necessite utilizar a tradução do texto, evitando assim erros residuais, além de possíveis erros com a biblioteca de tradução como ocorreu no Google Pegasus. Dessa forma, foi encontrado o algoritmo “mT5_multilingual_XLSum” disponível também no website “Hugging Face” publicado por [“csebuetnlp”](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum). Trata-se de um algoritmo originalmente desenvolvido pela Google, mas que foi ajustado utilizando a base de dados “XL-Sum” que, segundo os autores, é um conjunto de dados abrangente e diversificado que compreende 1 milhão de pares de artigos-resumo com anotações profissionais da BBC, extraídos usando um conjunto de heurísticas cuidadosamente projetadas. Dessa forma, o modelo multilíngue pré-treinado de última geração da Google, juntamente com o “XLSum” ajustado pelos autores possibilitou realizar a sumarização de qualidade em 44 idiomas diferentes. Por tal motivo, foi decidido utilizar esse modelo como principal nesse projeto de pesquisa.
