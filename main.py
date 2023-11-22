#from filtres import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter
image = Image.open("img/input/La_tour_Eiffel.jpeg")

image_paths = [
    "img/input/CS2.jpeg",
    "img/input/La_tour_Eiffel.jpeg",
    "img/input/MW3.jpeg"
]

def filtre_gris(image):
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,r,r))
    return nouvelle

image_filtree = filtre_gris(image)

image_filtree.save("img/output/imagenoirblanc.jpeg")

for img_path in image_paths:
    image = Image.open(img_path)

    image_filtree = filtre_gris(image)
    image_filtree.show()
    image_filtree.save("img/output/" + img_path.split("/")[-1].split(".")[0] + "_filtre_gris.jpg")

