#!/usr/local/bin/python3 python3
# Python 3.*

# Imports
# ------------------------------
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Chromosome import Chromosome
from Being import Being


gingerChromosome = Chromosome(
    name = "secondary",
    gene = "ginger"
)

blackChromosome = Chromosome(
    name = "secondary",
    gene = "black"
)

blondChromosome = Chromosome(
    name = "secondary",
    gene = "blond"
)

xChromosome = Chromosome(
    name = "gender",
    gene = "X")

yChromosome = Chromosome(
    name = "gender",
    gene = "Y")

originalGinger = Being("Joseph the brunette", [gingerChromosome, blackChromosome, yChromosome, xChromosome])
originalSlut = Being("Jackie's mother the ginger", [blackChromosome, blackChromosome, xChromosome, xChromosome])
originalFucker = Being("Zboub the blond", [blondChromosome, blondChromosome, xChromosome, yChromosome])

Jesus = originalGinger.mate(originalSlut, "Jesus")
Marie = Jesus.mate(originalFucker, "Marie")

#print(test.getName)
print(
    "The child of ", originalGinger.name
    , " with ", originalSlut.name
    , " is named "
    ,Jesus.name
    , "and it is "
    , Jesus.getChromosomesByNames()["gender"][0].getGene()
    , Jesus.getChromosomesByNames()["gender"][1].getGene()
    , Jesus.getChromosomesByNames()["secondary"][0].getGene()
    , Jesus.getChromosomesByNames()["secondary"][1].getGene()
    )
