import os
import subprocess
from tkinter import *
from tkinter import filedialog as fdialog
from tkinter import messagebox
import sys
from pytube import Playlist, YouTube

lista_url = []
es_playlist = False

# Recibe como parametro una lista de URL
def run(listavideos):
    contadorVideosBajados = 0
    
    print("Se han importado {} videos." .format(len(listavideos)))

    root = Tk()
    cuadroTexto = Label(root, text="Selecciona carpeta donde se van a guardar los videos", fg="red", font=("Helvetica", 16))
    cuadroTexto.pack()
    filepath = fdialog.askdirectory(title="Elige carpeta donde se van a guardar los videos")
    root.destroy()
    # get linked list of links in the playlist
    #links = pl.parse_links()
    # download each item in the list
    for url in listavideos:
        # converts the link to a YouTube object
        try:
            yt = YouTube(url)
        except KeyError:
            print("El video {} no está disponible" .format(contadorVideosBajados+1))
        except:
            print("Hubo algun problema con el video {}" .format(contadorVideosBajados+1))
        # takes first stream; since ffmpeg will convert to mp3 anyway
        music = yt.streams.first()
        # gets the filename of the first audio stream
        default_filename = music.default_filename
        print("\n\tDescargando " + default_filename + "...Por favor espera...")
        # downloads first audio stream
        music.download(filepath)

        # creates mp3 filename for downloaded file
        new_filename = default_filename[0:-3] + "mp3"
        print("Converting to mp3....")
        # converts mp4 audio to mp3 audio
        try:
            subprocess.run(['ffmpeg', '-y', '-i', 
            os.path.join(filepath, default_filename),
            os.path.join(filepath, new_filename)
            ])            
        except:
            print("Hubo algun problema descargando ", default_filename)

        #Elminamos el viejo video mp4
        print("Borramos el fichero de video...")
        os.remove(os.path.join(filepath,default_filename))


        contadorVideosBajados += 1
        print("Descargado {} de {}" .format(contadorVideosBajados,len(listavideos)))

    #Vaciamos el fichero para la siguiente vez
    fichero = open("1 - Pega aqui videos a descargar.txt",'w')
    fichero.truncate(0)
    fichero.close


if __name__ == "__main__":
    #ruta_fichero = input("Indica el fichero con las URL de playlist a descargar: ")
    
    # root = Tk()
    # root.filename =  fdialog.askopenfilename(title = "Selecciona fichero",filetypes = (("txt files","*.txt"),("all files","*.*")))    
    # fichero = open(root.filename,'r')
   
    try:
        fichero = open("1 - Pega aqui videos a descargar.txt",'r')
        urls_bruto = fichero.readlines()
        fichero.close()
    except:
        print("No se encuentra el fichero \"1 - Pega aqui videos a descargar.txt\"\nPega en el fichero los videos a descargar")
        messagebox.showinfo(message="No hay videos para descargar en el fichero", title="Fichero vacio")


    if len(urls_bruto) == 0:
        print("No hay videos para descargar en el fichero \"1 - Pega aqui videos a descargar.txt\"\nPega en el fichero los videos a descargar")
        messagebox.showinfo(message="No hay videos para descargar en el fichero", title="Fichero vacio")
        sys.exit(0)

    
    #root.destroy()

    for url in urls_bruto:
        es_playlist = False
        #Comprobamos si nos pasan una URL de video o de Playlist
        try:
            pl = Playlist(url)
            #En caso de exito añadimos cada URL a la lista de URL
            if len(pl) > 0:
                es_playlist = True            
        except KeyError:
            print("Importamos videos")            
        
        if es_playlist == True:
            for video in pl:
                lista_url.append(video)
        else:
            lista_url.append(url)    

    run(lista_url)
