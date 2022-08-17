#!/usr/bin/python3

def GestionDegats(Attaquant, Defenseur):
    Defenseur[1] = Defenseur[1] - (Attaquant[2] - Defenseur[3])
    return Defenseur
