#! usr/bin/env python

import random
import creerMonstre.py


def genMonstre(nom):
    pv = random.randrange(5, 21)
    force = random.randrange(3, 9)
    armure = random.randrange(0, 6)
    monstreTab = [nom, pv, force, armure]
