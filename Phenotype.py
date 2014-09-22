#!/usr/local/bin/python3 python3
# Python 3.*

# -*- coding: utf-8 -*-

# Imports
# ------------------------------
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Class
# ------------------------------
class Phenotype:
    """
    Phenotype of a being
    
    @args:
        Being: 
    
    """

    DATA = {
        "Human": set(["gender", "primary", "secondary", "sparkles", "beauty"]),
        "Bear": set(["gender", "primary", "secondary", "agressivity", "beauty"]),
        "Pork": set(["gender", "primary", "secondary", "sparkles", "bacon"]),
        "rock": set(["gender", "primary", "secondary", "preciousness"])
    }

    def __init__(self, being):
        self.being = being

    def getSpecie(self):
        beingChromosoms = self.being.getChromosomesNameSet()
        species = []
        for specieName, chromosomSet in self.DATA.items():
            if beingChromosoms.issuperset(chromosomSet):
                species.append(specieName)
        if not species:
            return "This being doesn't have a specie"
        species.sort()

        return "".join(species)
