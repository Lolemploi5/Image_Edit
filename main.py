from PIL import Image, ImageFilter, ImageDraw, ImageFont

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
    image_dilatation = image.filter(ImageFilter.MaxFilter(7))
    return image_dilatation

image_dilatation = dilatation_img(image)
image_dilatation.show()
image_dilatation.save("./img/output/img_dilatation.jpeg")

def rotate_img(image):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(25)
    return rotate_image

rotate_image = rotate_img(image)
rotate_image.show()
rotate_image.save("./img/output/img_rotate.jpeg")

def resize_img(image):
    # Redimensionner l'image selon des dimensions specifiées
    resize_image = image.resize((250, 250))
    return resize_image

resize_image = resize_img(image)
resize_image.show()
resize_image.save("./img/output/img_resize.jpeg")

def image_text(image):
    font = ImageFont.truetype("fonts/Gidole-Regular.ttf", 34)
    text = image.copy()
    draw = ImageDraw.Draw(text)
    draw.text((32, 20), "Hello Paris!", (255, 198, 32), font=font)
    return text

text_image = image_text(image)
text_image.show()
text_image.save("img/output/img_texte.png")









