from PIL import Image, ImageFilter
import logging

print("Entrez le path du fichier a traiter:")
img_path = input()
image = Image.open(img_path)
image.show()
def filtre_gris(image):
    nouvelle = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x,y))
            nouvelle.putpixel((x,y), (r,r,r))
    return nouvelle

image_filtree = filtre_gris(image)
image_filtree.show()
image_filtree.save("img/output/imagenoirblanc.jpeg")






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
image_dilatation.save("img/output/img_dilatation.jpeg")

#ar = angle de rotation
ars = input("Entrer l'angle de rotation :")
ar = int(ars)



def rotate_img(image):
    # Pivoter l'image selon un angle spécifié
    rotate_image = image.rotate(ar)
    return rotate_image

rotate_image = rotate_img(image)
rotate_image.show()
rotate_image.save("img/output/img_rotate.jpeg")

