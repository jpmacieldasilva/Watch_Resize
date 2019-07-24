import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import glob, math, os, shutil
from PIL import Image
imagesjpg=glob.glob("*.jpg")
imagespng=glob.glob("*.png")
numpng=str(len(imagespng))
numjpg=str(len(imagesjpg))

def on_create():
    ### Redimensionando JPG
    for imagejpg in imagesjpg:
        img=Image.open(imagejpg)

                # Calculo de redimensionamento mantendo a proporção
        width, height = img.size
        ratio = height/width
        newheight = int(ratio * 1920)

            # Calculo de redimensionamento mantendo a proporção
        img=img.resize((1920, newheight), Image.ANTIALIAS)

            #Criação do diretorio
        os.makedirs("otimizado", exist_ok=True)

            #Renomeando o arquivo
        filename='resized_'+imagejpg
        print(filename)

            #Salvando no diretorio
        img.save("otimizado/"+filename, format='JPEG')
        print("funfou") 

        print("Redimensionando os PNGs")

        #movendo o antigo para pasta old
        os.makedirs("old", exist_ok=True)
        shutil.move(imagejpg,"old")
        print("moveu") 

        ### Redimensionando PNG
    for imagepng in imagespng:
        img=Image.open(imagepng)

            # Calculo de redimensionamento mantendo a proporção
        width, height = img.size
        ratio = height/width
        newheight = int(ratio * 1920)

            # Calculo de redimensionamento mantendo a proporção
        img=img.resize((1920, newheight), Image.ANTIALIAS)         

            #Criação do diretorio
        os.makedirs("otimizado", exist_ok=True)

            #Renomeando o arquivo
        filename='resized_'+imagepng
        print(filename)

            #Salvando no diretorio
        img.save("otimizado/"+filename, format='PNG')
        print("funfou")
    
        #movendo o antigo para pasta old
        os.makedirs("old", exist_ok=True)
        shutil.move(imagepng,"old")
        print("moveu")   
 
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path="./", recursive=True)
    observer.start() 
    try:
        while True:
            on_create()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    