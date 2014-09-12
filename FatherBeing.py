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
class FatherBeing(Being):
    """
    Represent a father being
    Can be human or else
    
    @args:
        name: string, being name
        chromosoms: array of Chromosom objects
    """
    
    def __init__(self, name, chromosoms):
        super().__init__(name)
        
        self.chromosoms = chromosoms
