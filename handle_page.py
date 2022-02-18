import requests
from bs4 import BeautifulSoup
import sys
import json
import os
import unicodedata
import re

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

    def cleanText(self, text):
        text = text.replace('\n', ' ')
        cleanText = []
        # Parametro criado para auxiliar a remover referencias do  texto #
        ref = False
        for ch in text:
            if ref:
                pass
            elif ch == "[":
                ref = True
            elif ch == "]":
                ref = False
            else:
                nfkd = unicodedata.normalize('NFKD', ch)
                filter = re.sub('[^A-z 1-9 , . ( ) / : - -\\\]', '', nfkd)
                char = u"".join([c for c in filter if not unicodedata.combining(c)])
                cleanText.append(char)
        return ''.join(cleanText)

    def getTitulo(self):
        titulo = self.soup.title.string.split("–")[0].rstrip().lower()
        self.titulo = self.cleanText(titulo)       

    def getTexto(self):
        bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
        bodycontent = bodydiv.find_all(lambda tag: tag.name == 'p' and not tag.attrs)
        bodycontentfinal = ""
        for p in bodycontent[1:]:
            bodycontentfinal += p.get_text() + " "
        self.conteudo = self.cleanText(bodycontentfinal)
        
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