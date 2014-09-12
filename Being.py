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
            
            
    def getSpecie(self):
        return list(self.getChromosomsSet().keys())
    
    
    def geneticMix(self, chromosomsSets):
        """
        Mix any number of chromosoms sets
        The sets may come from different species
        
        @args:
            chromosomsSets: array of chromosoms sets
                chromosoms set: array of Chromosom objects
                
        @return:
            chromosoms list
        
        """
        
        # Retrieve all the unique chromosoms numbers from all the chromosoms sets
        chromosomsNumbers = set()
        for chromosomsSet in chromosomsSets:
            chromosomsNumbers = chromosomsNumbers.union(set(chromosomsSet.keys()))
        
        # Determine the mean number of chromosoms associated with each chromosom number
        # If the mean is not an integer, it will be randomly chosen among the two closest integers
        # The mean will be used as the expected quantity of chromosoms
        chromosomsQuantityByNumber = {}
        for chromosomNumber in chromosomsNumbers:
            mean = sum([len(chromosomsSet[chromosomNumber]) for chromosomsSet in chromosomsSets]) / len(chromosomsSets)
            
            intMean = int(mean)
            if not intMean == mean:
                intMean = random.chose([intMean, intMean + 1]) 
            
            chromosomsQuantityByNumber[chromosomNumber] = intMean
        
        # Pick a chromosom from each chromosom set if the number of sets equals the quantity of expected chromosoms
        # If it does not (degenerated chromosom mix), the chromosoms with a given number from all the sets will be pooled together,
        # then randomly drawn
        chromosomsSetsLength = len(chromosomsSets)
        chromosoms = []
        for chromosomNumber, chromosomQuantity in chromosomsQuantityByNumber.items():
            if chromosomQuantity == chromosomsSetsLength:
                # Regular chromosom mix
                for chromosomsSet in chromosomsSets:
                    chromosoms.append(random.choice(chromosomsSet[chromosomNumber]))
                    
            else:
                # Degenerated chromosom mix
                chromosomsPool = []
                for chromosomsSet in chromosomsSets:
                    chromosomsPool += chromosomsSet[chromosomNumber]
                    
                chromosoms += random.sample(chromosomsPool, chromosomQuantity)

        return chromosoms
