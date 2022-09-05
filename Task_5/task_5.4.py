# Kaupungin nimet

kaupungit = []

kaupungit_jäljellä = 5

while kaupungit_jäljellä > 0:
    kaupunki = str (input("Anna kaupunki:"))
    kaupungit_jäljellä-=1
    kaupungit.append(kaupunki)
if kaupungit_jäljellä == 0:
    for n in kaupungit:
        print(n)

