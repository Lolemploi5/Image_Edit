import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import logging

# Configuration du fchier de log
log_format = '%(asctime)s - %(levelname)s - %(message)s' #format des log affichés
logging.basicConfig(filename='main.log', level=logging.INFO, format=log_format)

image_paths = []

image = Image.open("img/input/La_tour_Eiffel.jpeg")

def applique_filtre(image, filtres):
    """
    Applique les filtres spécifiés à l'image.
    """
    for tout_filtre in filtres:
        parts = tout_filtre.split(':')
        type_filtre = parts[0]
        filter_value = int(parts[1]) if len(parts) > 1 else None

        if type_filtre == 'gris':
            image = filtre_gris(image)
        elif type_filtre == 'flou':
            image = filtre_flou(image)
        elif type_filtre == 'dilatation':
            image = dilatation_img(image)
        elif type_filtre == 'rotation':
            image = rotate_img(image, filter_value)
        elif type_filtre == 'resize':
            width, height = map(int, parts[1].split('&'))
            image = resize_img(image, width, height)
        elif type_filtre == 'texte':
            image = image_text(image, filter_value)
    return image

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

###################
####Filtre Flou####
###################

def filtre_flou(image):
    # Appliquer un filtre de flou
    image_flou = image.filter(ImageFilter.BLUR)
    return image_flou

##################
####Dilatation####
##################
def dilatation_img(image):
    # Appliquer une dilatation a l'image
    image_dilatation = image.filter(ImageFilter.MaxFilter(7))
    return image_dilatation

################
####Rotation####
################

def rotate_img(image, angle):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(angle)
    return rotate_image

#########################
####Redimentionnement####
#########################

def resize_img(image, width, height):
    # Redimensionner l'image selon des dimensions specifiées
    resize_image = image.resize((width, height))
    return resize_image

##################
####Image text####
##################

def image_text(image, text):
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    text_image = image.copy()
    draw = ImageDraw.Draw(text_image)
    draw.text((32, 20), text, (255, 198, 32), font=font)
    return text_image

def main():
    parser = argparse.ArgumentParser(description='Appliquer des filtres à une image.')
    parser.add_argument('--filters', type=str, help='Filtres à appliquer, séparés par "&". Par exemple, "gray&rotate:55"')
    parser.add_argument('--i', type=str, help='Dossier source qui contient les images initiales')
    parser.add_argument('--o', type=str, help='Dossier destination qui contiendra les images modifiées')

    args = parser.parse_args()

    if not args.filters or not args.i or not args.o:
        print("Veuillez spécifier les filtres, le dossier source et le dossier destination.")
        return

    filters = args.filters.split('&')
    try: #on verifie d'abord si nos arguments sont bons
        if not os.path.exists(args.i):
            raise FileNotFoundError(f"Le fichier source '{args.i}' n'existe pas.")
        elif not args.i.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            raise ValueError(f"Le fichier source '{args.i}' n'est pas une image valide.")

        image = Image.open(args.i)
        try: #on applique la fonction des filtres sur l'image
            image_filtree = applique_filtre(image, filters)
        except Exception as filter_error: #si ça marche pas on soulève une erreur
            print(f"Erreur lors de l'application des filtres : {filter_error}")

            # on ecrit l'erreur dans le fichier de log
            logging.error(f"Erreur lors de l'application des filtres : {filter_error}")
            return

        #on créé le nom de notre fichier de sortie
        chemin_sortie = os.path.join(args.o, f"{os.path.splitext(os.path.basename(args.i))[0]}_filtre.jpg")
        image_filtree.save(chemin_sortie)

        # on ecrit le succès dans notre fichier de log
        logging.info(f"Opération réussie : {filters} sur l'image {args.i}. Résultat sauvegardé dans {chemin_sortie}")

        #on affiche l'image
        image_filtree.show()

    except Exception as e: #on soulève les erreur précedentes et on les affiche dans le terminal
        print(f"Une erreur s'est produite : {e}")
        #on écrit les erreurs dans le fichier de log
        logging.error(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()