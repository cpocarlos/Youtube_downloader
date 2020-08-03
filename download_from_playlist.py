import os
import subprocess
from tkinter import *
from tkinter import filedialog as fdialog

from pytube import Playlist, YouTube

def run(pl):
    # get parent directory; VERY IMPORTANT!!
    # INCLUDE LAST SLASH AFTER FOLDER NAME
    # e.g. /home/username/Folder/ or C:\Users\Username\Folder\
    #filepath = input("Indica donde quieres guardar la musica:\n")
    root = Tk()
    filepath = fdialog.askdirectory(title="Carpeta Destino")
    root.destroy()
    # get linked list of links in the playlist
    #links = pl.parse_links()
    # download each item in the list
    for l in pl:
        # converts the link to a YouTube object
        yt = YouTube(l)
        # takes first stream; since ffmpeg will convert to mp3 anyway
        music = yt.streams.first()
        # gets the filename of the first audio stream
        default_filename = music.default_filename
        print("Descargando " + default_filename + "...")
        # downloads first audio stream
        music.download(filepath)
        print("Descargado")

if __name__ == "__main__":
    #ruta_fichero = input("Indica el fichero con las URL de playlist a descargar: ")
    root = Tk()
    root.filename =  fdialog.askopenfilename(title = "Selecciona fichero",filetypes = (("txt files","*.txt"),("all files","*.*")))    

    fichero = open(root.filename,'r')
    urls = fichero.read()

    fichero.close()
    root.destroy()

    #urls = urls_bruto.split()
    print("Se ha leido: \n", urls)
    pl = Playlist(urls)
    run(pl)
