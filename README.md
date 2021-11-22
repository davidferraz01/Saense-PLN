
# Saense PLN

#### Um projeto de Processamento de Linguagem Natural voltado ao site Saense

- **Objetivo atual:**
Esse projeto tem como objetivo inicial sumarizar os artigos encontrados na plataforma de divulgação científica [Saense](https://saense.com.br/) visando sua publicação em redes sociais, como Instagram, afim de alcançar um maior público. Visto que os textos publicados nessas plataformas apresentam-se de maneira bastante resumida.

- **Ideias futuras:**
Em seguida, temos intenção de implementar um algoritmo que identifique as palavras e sentenças mais importantes do texto, e futuramente encontrar relações entre os diversos artigos disponíveis no site, os agrupando.
Essas ferramentas irão ser de grande valia para uma **ideia futura** que consiste na criação de **Histórias em Quadrinhos** para distribuição em escolas públicas levando conteúdo científico de forma acessível e de maneira divertida.

- **O que temos atualmente:**
Por enquanto, temos o Crawler pronto. Tal algoritmo extrai com precisão os textos presentes no site do Saense, os salvando em arquivos ".txt", além disso salva informações extras em ".json" e imagens presentes no artigo que podem ser úteis nas próximas etapas do projeto.

## Como executar
Para executar o projeto, instale as dependências executando o comando:

    pip install -r requirements.txt

Pronto, basta executar o arquivo "handle_site.py", iniciando a extração dos dados:

    python3 handle_site.py <pag Incial> <pag Final>
**Obs.:** os argumentos "pag Inicial" e "pag Final" são números inteiros.
