#!/usr/local/bin/python3 python3
# Python 3.*

class Chromosom:
    """
    Represent a chromosom
    
    @args:
        number: integer, chromosom pair number
        gene: string, chromosom main gene
    
    """
    
    def __init__(self, number, gene):
        self.number = number
        self.gene = gene
    

    def getNumber(self):
        return self.number
    
    
    def getGene(self):
        return self.gene
