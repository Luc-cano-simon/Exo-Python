# on initialise la fonction randrange

from random import randrange

# on part de la valeur 0

initnombre = 0;

# on affiche le titre 

print("***Bienvenue dans le jeu du plus ou du moins en Python*** ");
print("\t\t Trouvez le nombre mystère compris entre 0 et 100");

# on definie la limite min et max pour trouver le numéro

nombreAleatoire = randrange(1,100);

# on boucle jusqu'a que le numéro soit trouvé

while initnombre != nombreAleatoire:

	print("Proposez un numéro ")

# On récupére la saisie de l'utilisateur et on lui dit que c'est un nombre entier

	initnombre = input()
	initnombre = int(initnombre)

	# si le nombre initiale est plus petit que le nombre aléatoire alors c'est plus 

	if initnombre < nombreAleatoire:
		print("c'est plus try again  ")

	# si le nombre initiale est plus grand que le nombre aléatoire alors c'est moins 

	elif initnombre > nombreAleatoire:
		print("c'est moins try again ")

	# Une fois le bon nombre trouvé on le signale à l'utilisateur
	else:
		print("c'est Gagné tu as trouvé le bon numéro ;) !! ")


