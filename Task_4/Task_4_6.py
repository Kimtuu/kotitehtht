import random


#kysytään nuolia, jotka osuu sisälle
pisteet_sisällä = int(input("Anna ympyrän sisälle osuneet pisteet:"))

#kysytään kaikkien heitettyjen nuolien arvoja
pisteet_heitetty = int(input("Anna pisteiden kokonaismäärä:"))

#iteroidaan nuolien määrälle
for i in range(0,pisteet_heitetty):
    x2 = random.uniform(-1.0,1.0)**2
    y2 = random.uniform(-1.0,1.0)**2
if x2+y2 < 1.0:

    pisteet_sisällä += 1

pii = (float (pisteet_sisällä)/(pisteet_heitetty)) * 4

print("piin liki arvo on", pii)

