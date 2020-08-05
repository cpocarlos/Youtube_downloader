import os
import subprocess
from tkinter import *
from tkinter import filedialog as fdialog

from pytube import Playlist, YouTube

lista_url = []
es_playlist = False

# Recibe como parametro una lista de URL
def run(listavideos):
    contadorVideosBajados = 0
    
    print("Se han importado {} videos." .format(len(listavideos)))

    root = Tk()
    filepath = fdialog.askdirectory(title="Carpeta Destino")
    root.destroy()
    # get linked list of links in the playlist
    #links = pl.parse_links()
    # download each item in the list
    for url in listavideos:
        # converts the link to a YouTube object
        yt = YouTube(l)
        # takes first stream; since ffmpeg will convert to mp3 anyway
        music = yt.streams.first()
        # gets the filename of the first audio stream
        default_filename = music.default_filename
        print("Descargando " + default_filename + "...")
        # downloads first audio stream
        music.download(filepath)
        contadorVideosBajados += 1
        print("Descargado {} de {}" .format(contadorVideosBajados,len(listavideos)))

if __name__ == "__main__":
    #ruta_fichero = input("Indica el fichero con las URL de playlist a descargar: ")
    root = Tk()
    root.filename =  fdialog.askopenfilename(title = "Selecciona fichero",filetypes = (("txt files","*.txt"),("all files","*.*")))    

    fichero = open(root.filename,'r')
    urls_bruto = fichero.readlines()

    fichero.close()
    root.destroy()

    for url in urls_bruto:
        es_playlist = False
        #Comprobamos si nos pasan una URL de video o de Playlist
        try:
            pl = Playlist(url)
            #En caso de exito añadimos cada URL a la lista de URL
            es_playlist = True            
        except KeyError:
            print("No se trataba de una playlist")
        
        if es_playlist == True:
            for video in pl:
                lista_url.append(video)
        else:
            lista_url.append(url)    

    run(lista_url)
