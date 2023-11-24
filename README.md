# Image_Edit
Dans le projet Python Image-Editor, le but est de pouvoir editer et appliquer plusieurs filtres sur des images.

## Liste des filtres
Il y a **6** filtres permettant de modifier des images:
-Le filtre Noir et blanc
-Le filtre flou
-Le filtre pour la dillatation
-Le filtre pour pivoter l'image
-Le filtre pour redimensionner l'image
-Le filtre pour écrire du texte sur l'image

## Liste des commandes
Pour pouvoir exécuter ces filtres voici les commandes suivantes :
'''
python3 main.py --filters "gris" --i img/input/cat.jpeg --o img/output
'''
'''
python3 main.py --filters "flou" --i img/input/cat.jpeg --o img/output
'''
'''
python3 main.py --filters "dilatation" --i img/input/cat.jpeg --o img/output
'''
'''
python3 main.py --filters "rotation:50" --i img/input/cat.jpeg --o img/output
'''
'''
python3 main.py --filters "texte" --i img/input/cat.jpeg --o img/output
'''
'''
python3 main.py --filters "taille:100x100" --i img/input/cat.jpeg --o img/output
'''



On peut exécuter plusieurs filtre en même temps en utilisant "&" pour séparer les filtres:
exemple : python3 main.py --filters "dilatation&rotation:50" --i img/input/cat.jpeg --o img/output