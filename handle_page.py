import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlsplit
from PIL import Image
import json
import os
import unicodedata
import re

class HandlePage:
    def __init__(self, url):
        self.url = url
        self.path_artigos = "./artigos"
        self.dict = {}
        self.titulo = None
        self.soup = None
        self.jsonobj = None
        self.text = None
        self.autor = None
        self.data = None
        self.image_url = None
        
    def getSoup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.soup = soup

    def cleanText(self, text):
        text = text.replace('\n', ' ')
        cleanText = []
        # Parametro criado para auxiliar a remover referencias do texto #
        ref = False
        for ch in text:
            if ch == "[":
                ref = True
            elif ch == "]":
                ref = False
            
            elif ref:
                pass
            else:
                nfkd = unicodedata.normalize('NFKD', ch)
                filter = re.sub('[^A-z 0-9 , . ( ) / - -\\\]', '', nfkd)
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
        self.text = self.cleanText(bodycontentfinal)
        
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
        f.write(self.text)
        f.close()
        #return True
    
    def saveImg(self):
        parts = urlsplit(self.image_url)
        paths = parts.path.split('/')
        formatoimg = "." + paths[::-1][0].split('.')[::-1][0]
        img = Image.open(requests.get(self.image_url, stream = True).raw)
        nomearquivoimg = self.titulo + formatoimg
        nomecompleto = os.path.join(self.path_artigos, nomearquivoimg)
        img.save(nomecompleto)

def main():
    # Funcao principal da aplicacao ##
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""
        Handle Page ( https://github.com/0xdferraz/Saense-PLN )
        Extrai o texto, imagem e informacoes de uma postagem do Saense ( https://saense.com.br/ )

        Uso: python handle_page.py <URL do Artigo>
        """)
        exit()
    else:
        url = sys.argv[1]

    page = HandlePage(url)

    # Executa os metodos necessarios para adquirir os dados #
    page.getSoup()
    page.getTitulo()
    print(page.titulo)
    page.getTexto() 
    page.getAutor()
    page.getData()
    page.getImageUrl()
    page.getJson()

    # Salva as informacoes #
    try:
        page.saveConteudo()
    except Exception as e:
        print("\nErro","'" + e + "'","ao salvar Texto", page.titulo)
    
    try:
        page.saveJson()
    except Exception as e:
        print("\nErro","'" + e + "'","ao salvar Json", page.titulo)

    try:
        page.saveImg()
    except Exception as e:
        print("\nErro","'" + e + "'","ao salvar Imagem", page.titulo)

    
    print("FIM.")
    
if __name__ == "__main__":
    main()