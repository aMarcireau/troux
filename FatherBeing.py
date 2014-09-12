#!/usr/local/bin/python3 python3
# Python 3.*

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
