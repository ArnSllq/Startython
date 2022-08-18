#!/usr/bin/python3

import genMonstre


def CreerMonstre():
    nom = input("Donnez un nom au monstre : ")
    return genMonstre.genMonstre(nom)
