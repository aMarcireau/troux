#!/usr/local/bin/python3 python3
# Python 3.*

# Imports
# ------------------------------
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Chromosom import Chromosom


# Class
# ------------------------------
class Being:
    """
    Represent a being
    Can be human or else
    
    @args:
        name: string, being name
        chromosoms: 
    
    """
    
    def __init__(self, name):
        self.name = name
        
        self.chromosoms = []


    def getName(self):
        return self.name()


    def getChromosoms(self):
        return self.chromosoms


    def getChromosomsSet(self):
        chromosomsSet = {}
        
        for chromosom in self.getChromosoms():
            if chromosom.getNumber() in chromosomsSet:
                chromosomsSet[chromosom.getNumber()].append(chromosom)
            else:
                chromosomsSet[chromosom.getNumber()] = [chromosom]
                
        return chromosomsSet
    
    
    def addChromosom(self, chromosom):
        self.chromosoms.append(chromosom)
        
        
    def removeChromosom(self, chromosom):
        self.chromosoms.remove(chromosom)
            
            
