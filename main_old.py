
from logger import *
#from filtres import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter


import art
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
"""
import time
import sys


animation = "|/-\\"
start_time = time.time()

def animation_1():
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 5:  # The animation will last for 10 seconds
                break
"""


#Liste des paths
image_paths = []
#Boucle Enter path
while True:
    #animation_1()
    path = input("\033[31m" + "Enter a path (or enter 'q' to quit): ")
    if path != "q":
        image_paths.append(path)
        logger.info('Path added [OK]')
    elif path == "q":
        logger.info('All path added [OK]')
        break







image = Image.open("img/input/La_tour_Eiffel.jpeg")


def applique_filtre(image, filtres):
    """
    Applique les filtres spécifiés à l'image.
    """
    for tout_filtre in filtres:
        parts = tout_filtre.split(':')
        part_text = tout_filtre.split(':')
        type_filtre = parts[0]
        filter_value = int(parts[1]) if len(parts) > 1 else None
        filter_text = part_text[1] if len(part_text) > 1 else None

        if type_filtre == 'gris':
            image = filtre_gris(image)
        elif type_filtre == 'flou':
            image = filtre_flou(image)
        elif type_filtre == 'dilatation':
            image = dilatation_img(image)
        elif type_filtre == 'rotation':
            if filter_value is not None:
                image = rotate_img(image, filter_value)
        elif type_filtre == 'resize':
            width, height = map(int, filter_value.split('/'))
            image = resize_img(image, width, height)
        elif type_filtre == 'texte':
            if filter_value is not None:
                image = image_text(image, filter_text)
    return image

###################
####Filtre gris####
###################
def filtre_gris(image):
    logger.info('Fonction filtre gris debut [OK]')
    #cimage = Copie de l'image
    cimage = image.copy()
    logger.info('Image filtre gris save [OK]')
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            #Definir la couleur grise
            cimage.putpixel((x,y), (r,r,r))
            logger.info('Filtre gris applique [OK]')
    return cimage

image_filtree = filtre_gris(image)

###################
####Filtre Flou####
###################
def filtre_flou(image):
    logger.info('Debut fonction filtre flou [OK]')
    # Appliquer un filtre de flou
    image_flou = image.filter(ImageFilter.BLUR)
    return image_flou

image_flou = filtre_flou(image)

##################
####Dilatation####
##################
def dilatation_img(image):
    # Appliquer une dilatation a l'image
    image_dilatation = image.filter(ImageFilter.MaxFilter(7))
    return image_dilatation

image_dilatation = dilatation_img(image)

################
####Rotation####
################

#ar = angle de rotation
ars = input("Entrer l'angle de rotation :")
#Convertion valeur
ar = int(ars)

def rotate_img(image):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(ar)
    return rotate_image

rotate_image = rotate_img(image)

#########################
####Redimentionnement####
#########################

#dimL = Dimention largeur
dimLi = input("Entrer la largeur de l'image :")
#Convertion valeur
dimL = int(dimLi)

#dimA = Dimention hauteur
dimAi = input("Entrer la hauteur de l'image :")
#Convertion valeur
dimA = int(dimAi)
def resize_img(image):
    # Redimensionner l'image selon des dimensions specifiées
    resize_image = image.resize((dimL, dimA))
    return resize_image

resize_image = resize_img(image)

##################
####Image text####
##################
#texti = Text input
texti = input("Entrez le texte a ajouter :")


def image_text(image):
    #Police d'ecriture
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    #Copie de l'image
    text = image.copy()
    #Convertir l'image en dessin
    draw = ImageDraw.Draw(text)
    #Placer le texte sur l'image
    draw.text((32, 20), texti, (255, 198, 32), font=font)
    return text


text_image = image_text(image)


#Boucle pour faire plusieurs images
for img_path in image_paths:
    #Liste des images
    image = Image.open(img_path)
#Filtre gris
    #Appel de la fonction
    image_filtree = filtre_gris(image)
    #Afficher l'image
    image_filtree.show()
    #Sauvegarde et nomination du fichier
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_gris.jpg")
#Filtre flou
    image_filtree = filtre_flou(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_flou.jpg")
#Dilatation
    image_filtree = dilatation_img(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_dilatation.jpg")
#Rotation
    image_filtree = rotate_img(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_rotation.jpg")
#Redimentionnement
    image_filtree = resize_img(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_resize.jpg")
#Image texte
    image_filtree = image_text(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_imgtxt.jpg")


