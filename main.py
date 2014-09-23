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

caucasian = Chromosome(
    name = "primary",
    gene = "caucasian")

sparklesClean = Chromosome(
    name = "sparkles",
    gene = "clean")

sparklesDisease = Chromosome(
    name = "sparkles",
    gene = "sparkles")

beautiful = Chromosome(
    name = "beauty",
    gene = "beautiful")

ugly = Chromosome(
    name = "beauty",
    gene = "ugly")

originalGinger = Being("Joseph the brunette", [gingerChromosome, blackChromosome, yChromosome, xChromosome, sparklesDisease, sparklesDisease, beautiful, beautiful, caucasian, caucasian])
originalSlut = Being("Jackie's mother the ginger", [blackChromosome, blackChromosome, xChromosome, xChromosome, sparklesDisease, sparklesDisease, beautiful, beautiful, caucasian, caucasian])
originalFucker = Being("Zboub the blond", [blondChromosome, blondChromosome, xChromosome, yChromosome, sparklesClean, sparklesClean, beautiful, beautiful, caucasian, caucasian])

Jesus = originalGinger.mate(originalSlut, "Jesus")
Marie = Jesus.mate(originalGinger, "Marie")


printList = [
    ["The child of", originalGinger.getName(), "with", originalSlut.getName(), "is named", Jesus.getName()],
    ["and it is:"], 
    ["   ", Jesus.getChromosomesByNames()["gender"][0].getGene(), Jesus.getChromosomesByNames()["gender"][1].getGene()],
    ["   ", Jesus.getChromosomesByNames()["secondary"][0].getGene(), Jesus.getChromosomesByNames()["secondary"][1].getGene()],
    ["   ", Jesus.getChromosomesByNames()["sparkles"][0].getGene(), Jesus.getChromosomesByNames()["sparkles"][1].getGene()],
    ["   ", Jesus.getChromosomesByNames()["beauty"][0].getGene(), Jesus.getChromosomesByNames()["beauty"][1].getGene()],
    ["Its specie is:", Jesus.getSpecie()],
    ["Are", originalGinger.getName(), "and", Jesus.getName(), "consanguineous?", str(Jesus.isConsanguineous(originalGinger))],
    ["Is", Jesus.getName(), "inbred?", str(Jesus.isInbred())],
    ["Is", Marie.getName(), "inbred?", str(Marie.isInbred())]
]

for printLine in printList:
    print(" ".join(printLine))
