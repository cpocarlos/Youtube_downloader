import os
import subprocess

from pytube import Playlist, YouTube

def run(pl):
    # get parent directory; VERY IMPORTANT!!
    # INCLUDE LAST SLASH AFTER FOLDER NAME
    # e.g. /home/username/Folder/ or C:\Users\Username\Folder\
    filepath = input("Indica donde quieres guardar la musica:\n")
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
        print("Downloading " + default_filename + "...")
        # downloads first audio stream
        music.download(filepath)
        # creates mp3 filename for downloaded file
        new_filename = default_filename[0:-3] + "mp3"
        print("Converting to mp3....")
        # converts mp4 audio to mp3 audio
        try:
            subprocess.run(['ffmpeg', '-i', 
            os.path.join(filepath, default_filename),
            os.path.join(filepath, new_filename)
            ])            
        except:
            print("Hubo algun problema descargando ", default_filename)

        #Elminamos el viejo video mp4
        print("Borramos el fichero de video...")
        os.remove(os.path.join(filepath,default_filename))
    
    print("Download finished.")

if __name__ == "__main__":
    ruta_fichero = input("Indica el fichero con las URL de videos a descargar: ")
    fichero = open(ruta_fichero,'r')
    urls_bruto = fichero.read()
    urls = urls_bruto.split()
    print("Se ha leido: \n", urls)
    #pl = Playlist(url)
    run(urls)
