#!/usr/local/bin/python3 python3
# Python 3.*

class ChildrenBeing(Being):
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
        
        self.chromosoms = self.geneticMixing()
