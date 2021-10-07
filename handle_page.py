import requests
from bs4 import BeautifulSoup
import sys
import json
import os

def getSoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def getTitulo(soup):
    titulo = soup.title.string.split("–")[0].rstrip()
    return titulo

def getTexto(soup):
    bodydiv = soup.body.find("div",{"itemprop":"articleBody"})
    bodycontent = bodydiv.find_all(lambda tag: tag.name == 'p' and not tag.attrs)
    bodycontentfinal = ""
    for p in bodycontent:
        bodycontentfinal += p.getText()
    return bodycontentfinal

def getAutor(soup):
    try:
        bodydiv = soup.body.find("div",{"itemprop":"articleBody"})
        autor, data = bodydiv.p.getText().split('\n')
    except Exception as e:
        autor = "Vazio"
        pass
    return autor

def getData(soup):
    try:
        bodydiv = soup.body.find("div",{"itemprop":"articleBody"})
        autor, data = bodydiv.p.getText().split('\n')
    except Exception as e:
        data = "Vazio"
        pass
    return data

def getImageUrl(soup):
    image_url = soup.find('figure').img['src']
    return image_url

def getJson(url,soup):
    dict = {
        "url": url,
        "titulo": getTitulo(soup),
        "autor": getAutor(soup),
        "data": getData(soup),
        "imgurl": getImageUrl(soup)
    }
    #json_object = json.dumps(dict, indent = 2) 
    return dict#json_object

def saveJson(jsonobj,titulo,path_artigos = ""):
    nomearquivo = titulo+".json"
    nomecompleto = os.path.join(path_artigos, nomearquivo)
    f = open(nomecompleto, "w", encoding = "ascii")
    json.dump(jsonobj, f, indent = 2)
    f.close()
    return True

def saveConteudo(conteudo,titulo,path_artigos = ""):
    nomearquivo = titulo+".txt"
    nomecompleto = os.path.join(path_artigos, nomearquivo)
    f = open(nomecompleto, "w")
    f.write(conteudo)
    f.close()
    return True

def main():
    """Função principal da aplicação.
    """
    print('Uso: python3 handle_page.py "<url do artigo>"')
    url = sys.argv[1]
    print(url)
    soup = getSoup(url)
    conteudo = getTexto(soup) 
    titulo = getTitulo(soup)
    print("Salvando conteúdo...")
    saveConteudo(conteudo,titulo)
    jsonobj = getJson(url,soup)
    print("Salvando JSON...")
    saveJson(jsonobj,titulo)
    print("FIM.")
    
if __name__ == "__main__":
    main()

## Conteudo: outra estratégia (mais genérica)
# import re
# textoCompleto = soup.get_text()
# index1 = textoCompleto.find("publicado em")+27
# index2 = textoCompleto.find('Como citar')
# textoRelevante = textoCompleto[index1:index2]
# textoLimpo = re.sub('[\n\t]', '', textoRelevante)
# print(textoLimpo)

# Salvar CSV contendo Titulo, Autor, Data, Imagem
# A partir do titulo, dá pra recuperar o arquivo .txt e .png/jpg
# .....