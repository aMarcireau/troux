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
from Phenotype import Phenotype


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
        
        self.phenotype = Phenotype(self)
        self.parents = []
        self.children = []


    def getName(self):
        return self.name
        
    
    def getChildren(self):
        return self.children
        
        
    def getParents(self):
        return self.parents
        
        
    def getPhenotype(self):
        return self.phenotype
        
        
    def addParent(self, being):
        self.parents.append(being)
        
    
    def addChild(self, being):
        self.children.append(being)

    
    def removeChild(self, being):
        self.children.remove(being)
        
    
    def removeParent(self, being):
        self.children.remove(being)
            
            
    def getChromosomes(self):
        return self.chromosomes
        

    def addChromosome(self, chromosome):
        self.chromosomes.append(chromosome)
        
        
    def removeChromosome(self, chromosome):
        self.chromosomes.remove(chromosome)


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


    def getSpecie(self):
        return self.phenotype.getSpecie()
        
        
    def isDescendant(self, being, maxDepth = 10, excludedBeings = []):
        if self == being:
            raise Exception("isDescendant cannot be called with self as argument")

        if being in self.parents:
            return True
            
        if not self.parents or not maxDepth:
            return False
        
        cleanedParents = [parent for parent in self.parents if not parent in excludedBeings]
        
        if not cleanedParents:
            return False
        
        return any([parent.isDescendant(being = being, maxDepth = maxDepth - 1, excludedBeings = excludedBeings + [self]) for parent in cleanedParents])
            

    def isAncestor(self, being, maxDepth = 10, excludedBeings = []):
        if self == being:
            raise Exception("isAncestor cannot be called with self as argument")
    
        if being in self.children:
            return True
            
        if not self.children or not maxDepth:
            return False
            
        cleanedChildren = [child for child in self.children if not child in excludedBeings]
        
        if not cleanedChildren:
            return False
        
        return any([child.isAncestor(being = being, maxDepth = maxDepth - 1, excludedBeings = excludedBeings + [self]) for child in cleanedChildren])
    
    
    def isConsanguineous(self, being, maxDepth = 10, excludedBeings = [], firstCall = True):
        if self == being:
            if firstCall:
                raise Exception("isConsanguineous cannot be called with self as argument")
            else:
                return True

        if self.isAncestor(being = being, maxDepth = maxDepth, excludedBeings = excludedBeings):
            return True    
        
        if not self.parents or not maxDepth:
            return False
            
        cleanedParents = [parent for parent in self.parents if not parent in excludedBeings]
        
        if not cleanedParents:
            return False
        
        return any([parent.isConsanguineous(being = being, maxDepth = maxDepth - 1, excludedBeings = excludedBeings + [self], firstCall = False) for parent in cleanedParents])
    
    
    def isInbred(self):
        return any([self.parents[0].isConsanguineous(otherParent) for otherParent in self.parents if not otherParent == self.parents[0]])


    def getGender(self):
        return Phenotype(self).getGender()


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
                    
        self.addChild(child)
        being.addChild(child)
        
        child.addParent(self)
        child.addParent(being)
    
        return child
