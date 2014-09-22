#!/usr/local/bin/python3 python3
# Python 3.*
# -*- coding: utf-8 -*-

# Class
# ------------------------------
class Chromosome:
    """
    Represent a chromosome
    
    @args:
        name: string, chromosome pair identifier
        gene: string, chromosome main gene
    
    """
    
    def __init__(self, name, gene):
        self.name = name
        self.gene = gene
    
    
    def __eq__(self, other):
        return self.getName() == other.getName() and self.getGene() == other.getGene()
        

    def getName(self):
        return self.name
    
    
    def getGene(self):
        return self.gene
