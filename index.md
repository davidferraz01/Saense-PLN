## Visão Geral

- **Objetivo atual:**
Esse projeto tem como objetivo inicial sumarizar os artigos encontrados na plataforma de divulgação científica [Saense](https://saense.com.br/) visando sua publicação em redes sociais, como Instagram, afim de alcançar um maior público. Visto que os textos publicados nessas plataformas apresentam-se de maneira bastante resumida.

- **Ideias futuras:**
Em seguida, temos intenção de implementar um algoritmo que identifique as palavras e sentenças mais importantes do texto, e futuramente encontrar relações entre os diversos artigos disponíveis no site, os agrupando.
Essas ferramentas irão ser de grande valia para uma **ideia futura** que consiste na criação de **Histórias em Quadrinhos** para distribuição em escolas públicas levando conteúdo científico de forma acessível e de maneira divertida.

- **O que temos atualmente:**
Por enquanto, temos o Crawler pronto e alguns algoritmos testes para sumarização dos textos. O algoritmo de Crawler extrai com precisão os textos presentes no site do Saense, os salvando em arquivos ".txt", além disso salva informações extras em ".json" e imagens presentes no artigo que podem ser úteis nas próximas etapas do projeto.

## Como executar
Para executar o projeto, instale as dependências executando o comando:

    pip install -r requirements.txt

Pronto, basta executar o arquivo "handle_site.py", iniciando a extração dos dados:

    python3 handle_site.py <pag Incial> <pag Final>



## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/0xdferraz/Saense-PLN/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/0xdferraz/Saense-PLN/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
