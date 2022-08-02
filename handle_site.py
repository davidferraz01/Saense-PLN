import requests
from bs4 import BeautifulSoup
import re
import os
import sys
from time import sleep
from handle_page import HandlePage
import json

class HandleSite():
    def __init__(self):
        self.path_artigos = "./artigos"
        self.URL = 'https://saense.com.br/page/'
        self.ini = None 
        self.fim = None
        self.lim = None
        self.Prim_Art = None
        self.Ult_Art = None

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
            ## Gerar lista de URLs dos artigos daquela pagina ##
            artigostags = soup.body.find_all("a",{"class": "o-overlayLink"})
            artigosurls = []
            for link in artigostags:
                artigosurls.append(link.get('href'))

            ## handle page ##
            for art in artigosurls:
                page = HandlePage(art)
                page.getSoup()
                page.getTitulo()

                temp = art.split('/')
                controle = temp[::-1][1]

                if page.titulo == primeiro:
                    a = False
                if a == True:
                    #print(controle)
                    if contador == 0:
                        controle_dict = {"primeiro": page.titulo, "ultimo": ""}
                    page.getTexto() 
                    page.getAutor()
                    page.getData()
                    page.getImageUrl()
                    page.getJson()

                    try: 
                        page.saveConteudo()
                    except Exception as e:
                        print("\nErro", e,"ao salvar Texto", page.titulo)
                    
                    try: 
                        page.saveJson()
                    except Exception as e:
                        print("\nErro", e,"ao salvar Json", page.titulo)

                    try: 
                        page.saveImg()
                    except Exception as e:
                        print("\nErro", e,"ao salvar Imagem", page.titulo)

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

    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""
        Handle Site ( https://github.com/0xdferraz/Saense-PLN )
        Extrai o texto, imagem e informacoes das postagens do Site Saense ( https://saense.com.br/ )

        Uso: python handle_site.py <Pagina Inicial> <Pagina Final>
        """)
        exit()
    else:
        site = HandleSite()

        site.ini = int(sys.argv[1]) #pagina inicial
        site.fim = int(sys.argv[2]) #pagina final
        site.lim = site.fim+1

        site.extract()
    
if __name__ == "__main__":
    main()