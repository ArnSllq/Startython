#!/usr/bin/python3

import Degat


def GestionCombat(Perso, Monstre):
    while Perso[1] > 0 and Monstre[1] > 0:
        Monstre = Degat.GestionDegats(Perso, Monstre)
        print(Monstre)
        Perso = Degat.GestionDegats(Monstre, Perso)
        print(Perso)
    return Perso
