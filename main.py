from logger import *
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os


image_paths = []

image = Image.open("img/input/cat.jpeg")

def applique_filtre(image, filtres):
#################################################
####Applique les filtres spécifiés à l'image.####
#################################################
    for tout_filtre in filtres:
        parts = tout_filtre.split(':')
        part_text = tout_filtre.split(':')
        type_filtre = parts[0]
        filter_value = int(parts[1]) if len(parts) > 1 else None
        filter_text = part_text[1] if len(part_text) > 1 else None

        if type_filtre == 'gris':
            image = filtre_gris(image)
            logger.info('Filtre gris set [OK]')
        elif type_filtre == 'flou':
            image = filtre_flou(image)
            logger.info('Filtre flou set [OK]')
        elif type_filtre == 'dilatation':
            image = dilatation_img(image)
            logger.info('Filtre dilatation set [OK]')
        elif type_filtre == 'rotation':
            if filter_value is not None:
                image = rotate_img(image, filter_value)
                logger.info('Filtre rotate set [OK]')
        elif type_filtre == 'resize':
            width, height = map(int, filter_value.split('/'))
            image = resize_img(image, width, height)
            logger.info('Filtre resize set [OK]')
        elif type_filtre == 'texte':
            if filter_value is not None:
                image = image_text(image, filter_text)
                logger.info('Filtre text set [OK]')
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
    logger.info('Image floutée [OK]')
    return image_flou

##################
####Dilatation####
##################
def dilatation_img(image):
    # Appliquer une dilatation a l'image
    image_dilatation = image.filter(ImageFilter.MaxFilter(7))
    logger.info('Image dilatée [OK]')
    return image_dilatation

################
####Rotation####
################

def rotate_img(image, angle):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(angle)
    logger.info('Image retournée [OK]')
    return rotate_image

#########################
####Redimentionnement####
#########################

def resize_img(image, width, height):
    # Redimensionner l'image selon des dimensions specifiées
    resize_image = image.resize((width, height))
    logger.info('Image redimentionée [OK]')
    return resize_image

##################
####Image text####
##################

def image_text(image, text):
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    text_image = image.copy()
    draw = ImageDraw.Draw(text_image)
    draw.text((32, 20), text, (255, 198, 32), font=font)
    logger.info('Texte ajouté  [OK]')
    return text_image

def main():
    parser = argparse.ArgumentParser(description='Appliquer des filtres à une image.')
    parser.add_argument('--filters', type=str, help='Filtres à appliquer, séparés par "&". Les filtres: gris, flou, dilatation, rotation, resize, texte. Exemple: "gray&rotate:55"')
    parser.add_argument('--i', type=str, help='Dossier source qui contient les images initiales')
    parser.add_argument('--o', type=str, help='Dossier destination qui contiendra les images modifiées')

    args = parser.parse_args()

    if not args.filters or not args.i or not args.o:
        print("Veuillez spécifier les filtres, le dossier source et le dossier destination.")
        logger.debug('Donnees spécifiées incorectes [KO]')
        return

    filters = args.filters.split('&')

    image = Image.open(args.i)
    image_filtree = applique_filtre(image, filters)
    image_filtree.show()
    logger.info('Résultat affiché [OK]')
    image_filtree.save(os.path.join(args.o, f"{os.path.splitext(os.path.basename(args.i))[0]}_filtre.jpg"))
    logger.info('Résultat sauvegardé [OK]')


if __name__ == "__main__":
    main()