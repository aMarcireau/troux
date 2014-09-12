#!/usr/local/bin/python3 python3
# Python 3.*

# Imports
# ------------------------------
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Chromosom import Chromosom
from FatherBeing import FatherBeing
from ChildBeing import ChildBeing

gingerChromosom = Chromosom(
    number = 1,
    gene = "ginger"
)

blackHairedChromosom = Chromosom(
    number = 1,
    gene = "blackHaired"
)

originalGinger = FatherBeing("Ronald", [gingerChromosom])
originalSlut = FatherBeing("P!nk", [blackHairedChromosom])


print(
    originalGinger.geneticMix([
        originalGinger.getChromosomsSet(), 
        originalSlut.getChromosomsSet()
    ])[0].getGene()
)
