#!/usr/bin/python3
#===============================================================================================================#
#---------------------------------------------------------------------------------------------------------------#
# Nom				:	CesarCode.py    																		#
# Description		:	Script permettant le chiffrement/dechiffrement d'un Code de Cesar						#
#																												#
# ENTREE																										#
#	Parametre(s)	:	n/a             																		#
#	Fichier(s)		:	n/a                                                      								#
#																												#
# Script(s) lance(s)	:	n/a                                             									#
#																												#
# SORTIE																										#
# 	Fichier(s)		:	n/a                                                              						#
# 	Code Retour		: 	0 = OK																					#
#						autre = KO																				#
#																												#
#===============================================================================================================#
# Version	| Date			| Modifications																		#
#---------------------------------------------------------------------------------------------------------------#
# 1.0		| 2022/07/31	| EN - Creation																		#
#---------------------------------------------------------------------------------------------------------------#
#===============================================================================================================#


# En cryptographie, le chiffrement par décalage, aussi connu comme le code de César est une méthode de chiffrement très simple.
# Le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet.
# Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début.


#========================#
# VARIABLES ET FONCTIONS #
#========================#
def regle_cesar(decalage):          # creation du dictionnaire associant l'alphabet à l'alphabet décalé
#    alphabet=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    alphabet=("0","b","j","â","4","o","à","1","p","ù","ë","a","6","k","ï","m","t","f","q","î","h","2","g","s","y","l","è","9","w","r","z","u","c","ê","n","é","v","5","d","3","8","x","û","ô","e","ü","7","i")
    id_lettre=0

    for lettre in alphabet:
        id_lettre=int(alphabet.index(lettre)+decalage)              # calcul de la nouvelle position de la lettre à partir de l'index de la lettre
        if id_lettre > (len(alphabet)-1):                           # si on depasse le nombre d'element de la liste, on revient au debut. -1 car le 1er element d'une liste est 0
            id_lettre-=len(alphabet)
        alphabet_mod[lettre]=alphabet[id_lettre]                    # on ajouter les differents element dans le dictionnaire
    # creation liste des cles
    #------------------------
    for cle in alphabet_mod.keys():		
        liste_cle.append(cle)

# Variables
#----------
valeur_decalage=0
alphabet_mod={}
liste_cle=[]
ajout=""
texte_mod=[]


#====================#
# DEBUT DU PROGRAMME #
#====================#
# boucle de saisi de l'utilisateur sur la valeur du decalage
while True:
    try:
        valeur_decalage=int(input("Saisissez la valeur de décalage pour chiffrer/déchiffrer le message [+ vers la droite ; - vers la gauche] : "))
        regle_cesar(valeur_decalage)

        texte=input("Saisissez votre texte :\n\t")
        for carac in texte.lower():
            if carac not in liste_cle:
                ajout=carac
            else:
                ajout=alphabet_mod[carac]
            texte_mod.append(ajout)

        print("Le texte modifié est le suivant:")
        print("\t"+''.join(texte_mod))
        break
    except:
        print("Valeur saisie incorrect\n")
        continue

#==================#
# FIN DU PROGRAMME #
#==================#