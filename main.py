#! usr/bin/env python

import Combat
import compteurEnnemi
import creerMonstre
import creerPerso
compteur = 0

pseudo = input("Quel est votre Pseudo : ")
pv = int(input("Quel est votre nombre de point de vie : "))
force = int(input("Quel est votre force : "))
armure = int(input("Quel est votre armure : "))

Perso = creerPerso.perso(pseudo, pv, force, armure)

while Perso[1] > 0:
    Monstre = creerMonstre.CreerMonstre()
    Perso = Combat.GestionCombat(Perso, Monstre)
    if Perso[1] > 0:
        compteur = compteurEnnemi.count(compteur, Perso)

print(compteur)
