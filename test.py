from PIL import Image, ImageDraw, ImageFont, ImageFilter


image_paths = [
    "img/input/CS2.jpeg",
    "img/input/La_tour_Eiffel.jpeg",
    "img/input/MW3.jpeg"
]

###################
####Filtre gris####
###################
def filtre_gris():
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,r,r))
    return nouvelle

image_filtree = filtre_gris(image)

image_filtree.save("img/output/imagenoirblanc.jpeg")`

##################################


image_paths = [
    "img/input/CS2.jpeg",
    "img/input/La_tour_Eiffel.jpeg",
    "img/input/cat.jpeg"
]
image = Image.open(path)
img/input/CS2.jpeg, img/input/La_tour_Eiffel.jpeg, img/input/cat.jpeg