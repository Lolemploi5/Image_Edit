#from filtres import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter

image_paths = []
while True:
    path = input("Enter a path (or enter 'q' to quit): ")
    if path != "q":
        image_paths.append(path)
        break
    elif path == "q":
        break







image = Image.open("img/input/La_tour_Eiffel.jpeg")


###################
####Filtre gris####
###################
def filtre_gris(image):
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,r,r))
    return nouvelle

image_filtree = filtre_gris(image)

###################
####Filtre Flou####
###################
def filtre_flou(image):
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
ar = int(ars)

def rotate_img(image):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(ar)
    return rotate_image

rotate_image = rotate_img(image)

#########################
####Redimentionnement####
#########################

dimLi = input("Entrer la largeur de l'image :")
dimL = int(dimLi)

dimAi = input("Entrer la hauteur de l'image :")
dimA = int(dimAi)
def resize_img(image):
    # Redimensionner l'image selon des dimensions specifiées
    resize_image = image.resize((dimL, dimA))
    return resize_image

resize_image = resize_img(image)

##################
####Image text####
##################

texti = input("Entrez le texte a ajouter :")


def image_text(image):
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    text = image.copy()
    draw = ImageDraw.Draw(text)
    draw.text((32, 20), texti, (255, 198, 32), font=font)
    return text


text_image = image_text(image)


#Boucle pour faire plusieurs images
for img_path in image_paths:
    image = Image.open(img_path)
#Filtre gris
    image_filtree = filtre_gris(image)
    image_filtree.show()
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


