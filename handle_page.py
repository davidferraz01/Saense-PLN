import requests
from bs4 import BeautifulSoup
import sys
import json
import os

class HandlePage:
    def __init__(self, url):
        self.url = url
        self.titulo = ""
        self.soup = ""
        self.path_artigos = ""
        self.jsonobj = ""
        self.conteudo = ""
        self.autor = ""
        self.data = ""
        self.image_url = ""
        self.dict = {}
    
    def getSoup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.soup = soup

    def getTitulo(self):
        titulo = self.soup.title.string.split("–")[0].rstrip()
        self.titulo = titulo

    def getTexto(self):
        bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
        bodycontent = bodydiv.find_all(lambda tag: tag.name == 'p' and not tag.attrs)
        bodycontentfinal = self.titulo + "\n"
        for p in bodycontent:
            bodycontentfinal += p.getText() + " "
        self.conteudo = bodycontentfinal

    def getAutor(self):
        try:
            bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
            autor, data = bodydiv.p.getText().split('\n')
        except Exception as e:
            autor = "Vazio"
            pass
        self.autor = autor

    def getData(self):
        try:
            bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
            autor, data = bodydiv.p.getText().split('\n')
        except Exception as e:
            data = "Vazio"
            pass
        self.data = data

    def getImageUrl(self):
        image_url = self.soup.find('figure').img['src']
        self.image_url = image_url

    def getJson(self):
        dict = {
            "url": self.url,
            "titulo": self.titulo,
            "autor": self.autor,
            "data": self.data,
            "imgurl": self.image_url
        }
        #json_object = json.dumps(dict, indent = 2) 
        self.dict = dict #jsonobj

    def saveJson(self):
        nomearquivo = self.titulo+".json"
        nomecompleto = os.path.join(self.path_artigos, nomearquivo)
        f = open(nomecompleto, "w", encoding = "ascii")
        json.dump(self.dict, f, indent = 2)
        f.close()
        #return True

    def saveConteudo(self):
        nomearquivo = self.titulo+".txt"
        nomecompleto = os.path.join(self.path_artigos, nomearquivo)
        f = open(nomecompleto, "w")
        f.write(self.conteudo)
        f.close()
        #return True

def main():
    # Funcao principal da aplicacao ##
    print('Uso: python3 handle_page.py "<url do artigo>"')
    url = sys.argv[1]

    page = HandlePage(url)

    print(url)

    # Executa os metodos necessarios para adquirir os dados #
    page.getSoup()
    page.getTitulo()
    page.getTexto() 
    page.getAutor()
    page.getData()
    page.getImageUrl()
    print("Salvando conteúdo...")
    page.saveConteudo()
    page.getJson()
    print("Salvando JSON...")
    page.saveJson()
    print("FIM.")
    
if __name__ == "__main__":
    main()

## Conteudo: outra estrategia (mais generica)
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