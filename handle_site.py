import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit
import os
import sys
from PIL import Image
from random import randint
from time import sleep
import handle_page as HP

# Salvar conteudo em arquivo
def saveTxt(conteudo,titulo,path_artigos = "./artigos"):
    nomearquivo = titulo+".txt"
    nomecompleto = os.path.join(path_artigos, nomearquivo)
    f = open(nomecompleto, "w")
    f.write(conteudo)
    f.close()
    return True

# Salvar arquivo de imagem
def saveImg(image_url,path_artigos = "./artigos"):
    ## Image name (salvar com nome do artigo)
    parts = urlsplit(image_url)
    paths = parts.path.split('/')
    formatoimg = paths[-1].split('.')[1]
    img = Image.open(requests.get(image_url, stream = True).raw)
    nomearquivoimg = titulo+"."+formatoimg
    nomecompleto = os.path.join(path_artigos, nomearquivoimg)
    img.save(nomecompleto)
    return True

def main():
    """Função principal da aplicação.
    """
    print('Uso: python3 handle_site.py <page_ini> <page_fim> <url do site>')
    URL = 'https://saense.com.br/page/' if (sys.argv[3] == "") else sys.argv[3]
    ## Acesso ao Saense principal e parsing
    #URL = 'https://saense.com.br/page/'
    ini = int(sys.argv[1]) #página inicial
    fim = int(sys.argv[2]) #página final
    lim = fim+1

    # Manter arquivo de controle das páginas já processadas
    path_artigos = "./artigos"
    nomearquivocontrole = "__controle.txt"
    nomecompleto = os.path.join(path_artigos, nomearquivocontrole)
    fcontrole = open(nomecompleto, "a+")
   
    ## Para cada página do portal principal...
    for page in range(ini,lim):
        fcontrole.write(str(page)+",")

        response = requests.get(URL+str(page)+'/')
        soup = BeautifulSoup(response.content, 'html.parser')
        ## Gerar lista de URLs dos artigos daquela página
        artigostags = soup.body.find_all("a",{"class": "o-overlayLink"})
        artigosurls = []
        for link in artigostags:
            artigosurls.append(link.get('href'))

        ## Para cada URL de artigo...
        for art in artigosurls:
            soup = HP.getSoup(art)
            titulo = HP.getTitulo(soup)
            conteudo = HP.getTexto(soup)
            jsonobj = HP.getJson(art,soup)
            #autor = HP.getAutor(soup)
            #data = HP.getData(soup)
            try: 
                HP.saveConteudo(conteudo,titulo,path_artigos) #salvar .txt
                HP.saveJson(jsonobj,titulo,path_artigos)
            except Exception as e:
                print(e)
                pass     
            #imgUrl = HP.getImageUrl(soup)
            #saveImg(imgUrl) #salvar .png/jpg/etc..
            print(".", end='', flush=True)
        print()
        sleep(randint(1,3))
        ## Evitar sobrecarregar servidor do portal com frequência alta de acessos
    ## FIM DO LAÇO
    fcontrole.close()
    print("FIM.")

if __name__ == "__main__":
    main()

## URL da página seguinte (talvez não precise)
#pgseguinteurl = soup.body.find("a",{"class": "next page-numbers"}).get('href')