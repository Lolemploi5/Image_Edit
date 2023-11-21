from PIL import Image, ImageFilter

image = Image.open("img/La_tour_Eiffel.jpeg")


def filtre_gris(image):
    # On fait une copie de l'image pour ne pas modifier l'original
    image_noir_blanc = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            image_noir_blanc.putpixel((x,y), (r,r,r))
    return image_noir_blanc

image_filtree = filtre_gris(image)
image_filtree.show()
image_filtree.save("./img/output/img_noir_blanc.jpeg")

def ajouter_filtre_flou(image):
    # Appliquer un filtre de flou
    image_flou = image.filter(ImageFilter.BLUR)
    return image_flou

image_flou = ajouter_filtre_flou(image)
image_flou.show()
image_flou.save("./img/output/img_flou.jpeg")

def dilatation_img(image):
    # Appliquer une dilatation a l'image
    image_dilatation = image.filter(ImageFilter.MaxFilter(8))
    return image_dilatation

image_dilatation = dilatation_img(image)
image_dilatation.show()
image_dilatation.save("./img/output/img_dilatation.jpeg")


