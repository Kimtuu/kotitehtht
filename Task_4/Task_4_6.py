import random


#kysytään nuolia, jotka osuu sisälle
nuolet_sisällä = int(input("Anna ympyrän sisälle osuneet nuolet:"))

#kysytään kaikkien heitettyjen nuolien arvoja
nuolet_heitetty = int(input("Anna heitettyjen nuolien kokonaismäärä:"))

#iteroidaan nuolien määrälle
for i in range(0,nuolet_heitetty):
    x2 = random.uniform(-1.0,1.0)**2
    y2 = random.uniform(-1.0,1.0)**2
if x2+y2 < 1.0:

    nuolet_sisällä += 1

pii = (float (nuolet_sisällä)/(nuolet_heitetty)) * 4

print("piin liki arvo on", pii)

