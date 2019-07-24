import glob, math, os, shutil
from PIL import Image
imagesjpg=glob.glob("*.jpg")
imagespng=glob.glob("*.png")
numpng=str(len(imagespng))
numjpg=str(len(imagesjpg))

print("Você tem "+numjpg+" JPGs e "+numpng+" PNGs")

print("Redimensionando os JPGs")
### Redimensionando JPG
for image in imagesjpg:
    img=Image.open(image)

# Calculo de redimensionamento mantendo a proporção
    width, height = img.size
    ratio = height/width
    newheight = int(ratio * 1920)

# Calculo de redimensionamento mantendo a proporção
    img=img.resize((1920, newheight), Image.ANTIALIAS)

#movendo o antigo para pasta old
    os.makedirs("old", exist_ok=True)
    shutil.move(image,"old")
    print("moveu")    

#Criação do diretorio
    os.makedirs("otimizado", exist_ok=True)

#Renomeando o arquivo
    filename='resized_'+image
    print(filename)

#Salvando no diretorio
    img.save("otimizado/"+filename, format='JPEG')
    print("funfou")

print("Redimensionando os PNGs")

### Redimensionando PNG
for image in imagespng:
    img=Image.open(image)

# Calculo de redimensionamento mantendo a proporção
    width, height = img.size
    ratio = height/width
    newheight = int(ratio * 1920)

# Calculo de redimensionamento mantendo a proporção
    img=img.resize((1920, newheight), Image.ANTIALIAS)  

#Criação do diretorio
    os.makedirs("otimizado", exist_ok=True)

#Renomeando o arquivo
    filename='resized_'+image
    print(filename)

#Salvando no diretorio
    img.save("otimizado/"+filename, format='PNG')
    print("funfou")


