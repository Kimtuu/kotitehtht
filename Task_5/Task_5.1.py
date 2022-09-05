#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random
summa = []
#kysytään noppien määrää
nopat = int (input("montako noppaa heitetään?:"))

for i in range (nopat):
    noppa = random.randint(1,6)
    summa.append(noppa)
    print(noppa)
print("heitettyjen noppien summa on:")
print (sum(summa))