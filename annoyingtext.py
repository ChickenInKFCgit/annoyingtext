import os
from random import randint

def codertexte(texte):
	res = ""
	for lettre in texte:
		if lettre in Lettres:
			possibilites = Lettres[lettre]
			choisie = randint(0, len(possibilites)-1)

			res+=possibilites[choisie]
		else:
			res+=lettre
	return res


def load_dict_lettres():
	d = {}

	f = open(PATH_LETTRES, mode="r",encoding=ENCODING)
	for ligne in f.read().split("\n"):
		possibilites = ligne.split("\t")
		lettre = possibilites.pop(0)
		d[lettre] = possibilites
	
	return d
			


def save_dict_lettres():
	f = open(PATH_LETTRES, mode="w+",encoding=ENCODING)
	for lettre in Lettres.keys():
		ligne = f"\n{lettre}"
		for variation in Lettres[lettre]:
			ligne+=f"\t{variation}"
		f.write(ligne)

# déplacement de "l'exécuteur" du script python vers le dossier courant.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PATH_LETTRES = os.path.abspath("lettres.tsv")
ENCODING = "utf-16"
Lettres = load_dict_lettres()