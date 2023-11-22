#from filtres import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter
texti = input("Entrez le texte a ajouter :")
image = Image.open("img/input/La_tour_Eiffel.jpeg")
def image_text(image):
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    text = image.copy()
    draw = ImageDraw.Draw(text)
    draw.text((32, 20), texti, (255, 198, 32), font=font)
    return text


text_image = image_text(image)
text_image.show()
text_image.save("img/output/img_texte.png")



"""
def appliquer_filtres_sur_images(liste_images):
    for chemin_image in liste_images:
        # Charger l'image
        image = Image.open(chemin_image)

        # Appliquer le filtre noir et blanc
        image_noir_blanc = filtre_gris(image)

        # Appliquer le filtre de flou à l'image en noir et blanc
        image_floue = ajouter_filtre_flou(image)

        # Appliquer la rotation à l'image floutée
        image_rotated = rotate_img(image)

        # Sauvegarder l'image résultante
        chemin_sortie = f"img/output/{chemin_image.split('/')[-1].split('.')[0]}_resultat.jpg"
        image_rotated.save(chemin_sortie)

if main.py == "filtres.py":
    # Liste des chemins vers les images
    liste_images = ["img/input/La_tour_Eiffel.jpeg", "img/input/CS2.jpeg", "img/input/MW3.jpeg"]

    # Appliquer les filtres sur toutes les images
    appliquer_filtres_sur_images(liste_images)
"""