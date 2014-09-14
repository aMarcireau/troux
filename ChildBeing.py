#!/usr/local/bin/python3 python3
# Python 3.*

# Imports
# ------------------------------
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Being import Being


# Class
# ------------------------------
class ChildBeing(Being):
    """
    Represent a children being
    Can be human or else
    
    @args:
        name: string, being name
        parents: array of Being objects   
    
    """

    def __init__(self, name, parents):
        self.parents = parents
        
        super().__init__(name)
        
        self.chromosoms = self.geneticMixing([parent.getChromosomsSet() for parent in self.getParents()])
        


    def getParents(self):
        return self.parents
