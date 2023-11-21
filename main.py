
from PIL import Image

image = Image.open("La_tour_Eiffel.jpeg")

image.show()

def filtre_rouge(image):
    # On fait une copie de l'image pour ne pas modifier l'original
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,0,0))
    return nouvelle

image_filtree = filtre_rouge(image)
image_filtree.show()