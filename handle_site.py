import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit
import os
import sys
from PIL import Image
from random import randint
from time import sleep
from handle_page import HandlePage

class HandleSite():
    def __init__(self):
        self.path_artigos = "./artigos"
        self.conteudo = ""
        self.titulo = ""
        self.image_url = ""
        self.ini = 0
        self.fim = 0
        self.lim = 0
        self.URL = ""

    # Salvar conteudo em arquivo #
    def saveTxt(self):
        nomearquivo = self.titulo+".txt"
        nomecompleto = os.path.join(self.path_artigos, nomearquivo)
        f = open(nomecompleto, "w")
        f.write(self.conteudo)
        f.close()
        return True

    # Salvar arquivo de imagem #
    def saveImg(self):
        parts = urlsplit(self.image_url)
        paths = parts.path.split('/')
        formatoimg = paths[::-1][0].split('.')[::-1][0]
        img = Image.open(requests.get(self.image_url, stream = True).raw)
        nomearquivoimg = self.titulo + "." + formatoimg
        nomecompleto = os.path.join(self.path_artigos, nomearquivoimg)
        img.save(nomecompleto, formatoimg)
        return True

    def extract(self):

        nomearquivocontrole = "__controle.txt"
        nomecompleto = os.path.join(self.path_artigos, nomearquivocontrole)
        fcontrole = open(nomecompleto, "a+")

        for page in range(self.ini,self.lim):
            fcontrole.write(str(page)+",")

            response = requests.get(self.URL+str(page)+'/')
            soup = BeautifulSoup(response.content, 'html.parser')
            ## Gerar lista de URLs dos artigos daquela pagina
            artigostags = soup.body.find_all("a",{"class": "o-overlayLink"})
            artigosurls = []
            for link in artigostags:
                artigosurls.append(link.get('href'))

            ## handle page ##
            for art in artigosurls:
                page = HandlePage(art)
                # Executa os metodos necessarios para adquirir os dados #
                page.path_artigos = self.path_artigos
                page.getSoup()
                page.getTitulo()
                page.getTexto() 
                page.getAutor()
                page.getData()
                page.getImageUrl()
                page.getJson()
                self.titulo = page.titulo
                self.image_url = page.image_url
                self.saveImg() #salvar .png/jpg/etc..

                try: 
                    page.saveConteudo() #salvar .txt
                    page.saveJson()
                except Exception as e:
                    print(e)
                    pass    

                print(".", end = '', flush=True)
            print()
            sleep(randint(1,3))
            ## Evitar sobrecarregar servidor do portal com frequencia alta de acessos ##
        fcontrole.close()
        print("FIM.")

def main():
    ## Funcao principal da aplicacao. ##
    print('Uso: python3 handle_site.py <page_ini> <page_fim> <url do site>')

    site = HandleSite()

    site.URL = 'https://saense.com.br/page/' if (sys.argv[3] == "") else sys.argv[3]

    ## Acesso ao Saense principal e parsing
    # URL = 'https://saense.com.br/page/'
    site.ini = int(sys.argv[1]) #pagina inicial
    site.fim = int(sys.argv[2]) #pagina final
    site.lim = site.fim+1

    site.extract()
    
if __name__ == "__main__":
    main()

## URL da pagina seguinte (talvez não precise)
#pgseguinteurl = soup.body.find("a",{"class": "next page-numbers"}).get('href')