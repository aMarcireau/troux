#!/usr/local/bin/python3 python3
# Python 3.*

# -*- coding: utf-8 -*-

# Imports
# ------------------------------
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Chromosome import Chromosome



# Class
# ------------------------------
class Being:
    """
    Represent a being
    Can be human or else
    
    @args:
        name: string, being name
        chromosomes: 
    
    """
    
    def __init__(self, name, chromosomes):
        self.name = name
    
        self.chromosomes = chromosomes


    def getName(self):
        return self.name()


    def getChromosomes(self):
        return self.chromosomes


    def getChromosomesByNames(self):
        chromosomesByNames = {}
        
        for chromosome in self.getChromosomes():

            if chromosome.getName() in chromosomesByNames:
                chromosomesByNames[chromosome.getName()].append(chromosome)
            else:
                #Python implicitely creates a key whenever you declare a property on a key that doesn't exist
                chromosomesByNames[chromosome.getName()] = [chromosome] 
                
        return chromosomesByNames
    

    def getChromosomesNameSet(self):
        return set(self.getChromosomesByNames().keys())


    def addChromosome(self, chromosome):
        self.chromosomes.append(chromosome)
        
        
    def removeChromosome(self, chromosome):
        self.chromosomes.remove(chromosome)


    def mate(self, being, name):
        child = Being(name, [])

        # Declaration of sets of chromosomes for each being
        intersectionSet = self.getChromosomesNameSet().intersection(being.getChromosomesNameSet())
        selfUniqueSet = self.getChromosomesNameSet().difference(being.getChromosomesNameSet())
        beingUniqueSet = being.getChromosomesNameSet().difference(self.getChromosomesNameSet())

        for chromosomeName in intersectionSet:

            for individual in [self, being]:
                chromosomes = individual.getChromosomesByNames()[chromosomeName]
                chromosomesMean = len(chromosomes) / 2

                #selectionSize is the number of chromosomes each parent is giving to his child for a certain chromosome type. It is used to create trisomic children
                if (chromosomesMean % 2 == 0):
                    selectionSize = int(chromosomesMean)

                else:
                    selectionSize = random.choice([int(chromosomesMean), int(chromosomesMean) + 1])

                #Randomly choose a certain number of chromosomes (number = selectionSize)
                for chromosome in random.sample(chromosomes, selectionSize):
                    child.addChromosome(chromosome)

        for individual, individualUniqueSet in [(self, selfUniqueSet), (being, selfUniqueSet)]:

            for chromosomeName in individualUniqueSet:
                chromosomes = individual.getChromosomesByNames()[chromosomeName]

                for chromosome in chromosomes:
                    child.addChromosome(chromosome)
    
        return child
