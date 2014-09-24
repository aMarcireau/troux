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

    GENES = {
        "primary": [("caucasian", 1), ("black", 3), ("arabic", 2), ("asian", 3)],
        "secondary": [("black", 3), ("blond", 2), ("ginger", 1)],
        "sparkles": [("clean", 3), ("sparkles", 1)],
        "beauty": [("beautiful", 2), ("ugly", 2)],
        "gender": [("X", 2), ("Y", 2)],
        "agressivity": [("agressive", 3), ("passive", 1)],
        "bacon": [("baconfat", 3), ("baconlight", 1)],
        "preciousness": [("regular", 3), ("precious", 1)]
    }

    GENDERDATA = { "man": ["X", "Y"], "woman": ["X", "X"],
    "alphamanYY": ["Y", "Y"], "trisomanXXY": ["X", "X", "Y"], "trisowomanXXX": ["X", "X","X"], "trisoalphamanYYX": ["Y", "Y", "X"], "trisoalphamanYYY": ["Y", "Y", "Y"]
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

    def getGender(self):
        for key in self.GENDERDATA.keys():
        	if len([chromosome.getGene() for chromosome in self.being.getChromosomesByNames()["gender"]]) > 3:
        		return "you have 4 gender chromosome, you should be dead!"

        	else:
	            if sorted([chromosome.getGene() for chromosome in self.being.getChromosomesByNames()["gender"]]) == sorted(self.GENDERDATA[key]):
	        
	                print( [chromosome.getGene() for chromosome in self.being.getChromosomesByNames()["gender"]])

	                return key

        return "unknown"
