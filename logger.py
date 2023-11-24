from main import *

import logging
import sys

# Configuration du fichier de logs
logging.basicConfig(level=logging.DEBUG,
                    filename="main.log",
                    filemode="w",
                    format="%(asctime)s, %(name)s %(levelname)s %(message)s")

# Création du logger
logger = logging.getLogger('IE_Logger')

# Création d'un StreamHandler pour la console
console_handler = logging.StreamHandler(sys.stdout)

# Définition du niveau de log pour le handler de la console
console_handler.setLevel(logging.WARNING)

# Ajout du handler de la console au logger
logger.addHandler(console_handler)


test = True
if test == True:
   try:
      logger.info('IE_Logger est operationnel [OK]')
   except:
      logger.warning('Test log 1 [KO]')





