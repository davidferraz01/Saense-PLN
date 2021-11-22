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
import json

class HandleSite():
    def __init__(self):
        self.path_artigos = "./artigos"
        self.conteudo = ""
        self.titulo = ""
        self.image_url = ""
        self.ini = 0
        self.fim = 0
        self.lim = 0
        self.URL = 'https://saense.com.br/page/'
        self.Prim_Art = ""
        self.Ult_Art = ""

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

        nomejsoncontrole = "__controle.json"
        nomecompletojson = os.path.join(self.path_artigos, nomejsoncontrole)

        try:
            with open(nomecompletojson) as jfile:
                jdata = json.load(jfile)
                primeiro = jdata["primeiro"]
                ultimo = jdata["ultimo"]
        except: #json.decoder.JSONDecodeError:
            jdata = open(nomecompletojson, "a+")
            dict = {"primeiro": " ", "ultimo": " "}
            json.dump(dict, jdata, indent=2)
            primeiro = " "
            ultimo = " "

        ## Iniciando variaveis auxiliares ##
        a = True
        contador = 0
        controle_dict = {"primeiro": primeiro, "ultimo": ultimo}
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
                page.path_artigos = self.path_artigos
                page.getSoup()
                page.getTitulo()

                temp = art.split('/')
                controle = temp[::-1][1]

                if page.titulo == primeiro:
                    a = False
                if a == True:
                    print(controle)
                    if contador == 0:
                        controle_dict = {"primeiro": page.titulo, "ultimo": ""}
                    page.getTexto() 
                    page.getAutor()
                    page.getData()
                    page.getImageUrl()
                    page.getJson()
                    self.titulo = page.titulo
                    self.image_url = page.image_url
                    self.saveImg()

                    try: 
                        page.saveConteudo()
                        page.saveJson()
                    except Exception as e:
                        print(e)

                if page.titulo == ultimo:
                    a = True
                
                contador += 1
                print(".", end = '', flush=True)
                
            print()

            ## Evitar sobrecarregar servidor do portal com frequencia alta de acessos ##
            sleep(1)
        ## local variable 'controle_dict' referenced before assignment ##
        controle_dict["ultimo"] = page.titulo
        jcontrole = open(nomecompletojson, "w")
        json.dump(controle_dict, jcontrole, indent=2)
        
        fcontrole.close()
        print("FIM.")

def main():
    print('Uso: python3 handle_site.py <page_ini> <page_fim>')

    site = HandleSite()

    site.ini = int(sys.argv[1]) #pagina inicial
    site.fim = int(sys.argv[2]) #pagina final
    site.lim = site.fim+1

    site.extract()
    
if __name__ == "__main__":
    main()