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
# 2.0		| 2022/08/03	| EN - Ajout d'une IHM																#
#---------------------------------------------------------------------------------------------------------------#
#===============================================================================================================#


# En cryptographie, le chiffrement par décalage, aussi connu comme le code de César est une méthode de chiffrement très simple.
# Le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet.
# Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début.


#==========#
# PACKAGES #
#==========#
from tkinter import *
from functools import partial


#========================#
# VARIABLES ET FONCTIONS #
#========================#
def update_label(label, text):
    label.config(text=text,fg='green')

# Fonction pour la creation du dictionnaire associant l'alphabet à l'alphabet décalé
#-----------------------------------------------------------------------------------
def regle_cesar(decalage):
    alphabet=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
#    alphabet=("0","b","j","â","4","o","à","1","p","ù","ë","a","6","k","ï","m","t","f","q","î","h","2","g","s","y","l","è","9","w","r","z","u","c","ê","n","é","v","5","d","3","8","x","û","ô","e","ü","7","i")
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
    return liste_cle

# Fonction principale pour chiffrer/dechiffrer
#---------------------------------------------
def chiffrage():
    decalage=scale_value.get()
    texte=str(widget_saisi.get())
    texte_mod=[]
    ajout=""
    texte_modifie=""

    # creation de la regle de cesar: decalage des lettres
    # par rapport à l'alphabet
    #----------------------------------------------------
    regle_cesar(decalage)

    # modification du texte
    #----------------------
    for carac in texte.lower():
        if carac not in liste_cle:
            ajout=carac
        else:
            ajout=alphabet_mod[carac]
        texte_mod.append(ajout)

    texte_modifie=''.join(texte_mod)                # on transforme la liste en chaine de caractère
    update_label(widget_label_final,texte_modifie)

# Variables
#----------
alphabet_mod={}
liste_cle=[]


#====================#
# DEBUT DU PROGRAMME #
#====================#
root=Tk()
root.title('Code de Cesar')

# Zone de texte
#--------------
Label(root,text="Code de Cesar").grid(column=1,row=0)
Label(root,text="Le code de César (ou chiffrement par décalage) est une méthode de chiffrement qui s'obtient en remplaçant\nchaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet\n").grid(column=0,row=1)

# zone de saisi texte à chiffrer/dechiffrer
#------------------------------------------
Label(root,text="Saisissez votre texte :").grid (column=0,row=2)
widget_saisi=Entry(root, textvariable=StringVar(), width=100)
widget_saisi.grid(column=0,row=3)

# zone du choix de décalage
#--------------------------
Label(root,text="Saisissez votre décalage :").grid (column=2,row=2)
scale_value=IntVar()
widget_scale=Scale(root, from_=-15, to=15, showvalue=True, variable=scale_value, length=200, tickinterval=5, orient='h')
widget_scale.grid(column=2,row=3)

# bouton pour chiffrer/dechiffrer
#--------------------------------
widget_label_final=Label(root,text="Texte modifié",fg='red',state="active")
widget_label_final.grid (column=0,row=5)

# bouton pour chiffrer/dechiffrer
#--------------------------------
Button(root,text='Chiffrer/Dechiffrer',command=chiffrage).grid(column=1,row=4)

root.mainloop()
#==================#
# FIN DU PROGRAMME #
#==================#