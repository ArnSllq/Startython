#!/usr/bin/python3

import creerMonstre.py, creerPerso.py, Degat.py

def GestionCombat(Perso, Monstre):
    while Perso[1] > 0 and Monstre[1] > 0:
        Monstre = GestionDegats(Perso, Monstre)
        Perso = GestionDegats(Monstre, Perso)
    return Perso
