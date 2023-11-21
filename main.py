from PIL import Image

image = Image.open("img/La_tour_Eiffel.jpeg")


def filtre_gris(image):
    # On fait une copie de l'image pour ne pas modifier l'original
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,r,r))
    return nouvelle

image_filtree = filtre_gris(image)
image_filtree.show()
image_filtree.save("img/output/output.jpeg")


