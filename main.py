#!/usr/local/bin/python3 python3
# Python 3.*

# Imports
# ------------------------------
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Chromosom import Chromosom
from Being import Being


gingerChromosom = Chromosom(
    number = 1,
    gene = "ginger"
)

blackHairedChromosom = Chromosom(
    number = 1,
    gene = "blackHaired"
)

blondHairedChromosom = Chromosom(
    number = 1,
    gene = "blondHaired"
)

xChromosom = Chromosom(
    number = 2,
    gene = "X chromosom")

yChromosom = Chromosom(
    number = 2,
    gene = "Y chromosom")

originalGinger = Being("Joseph the blackhaired", [gingerChromosom, blackHairedChromosom, yChromosom, xChromosom])
originalSlut = Being("Jackie's mother the ginger", [blackHairedChromosom, blackHairedChromosom, xChromosom, xChromosom])
originalFucker = Being("Zboub the blondhaired", [blondHairedChromosom, blondHairedChromosom, xChromosom, yChromosom])

Jesus = originalGinger.mate(originalSlut, "Jesus")
Marie = Jesus.mate(originalFucker, "Marie")

#print(test.getName)
print(
    "The child of ", originalGinger.name
    , " with ", originalSlut.name
    , " is named "
    ,Jesus.name
    , "and it is "
    , Jesus.getChromosomsSet()[1][0].getGene()
    , Jesus.getChromosomsSet()[1][1].getGene()
    )
