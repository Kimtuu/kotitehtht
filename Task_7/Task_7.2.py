nimi_joukko = set()

nimi = str(input("Anna nimi:"))

while nimi != "":
    if nimi not in nimi_joukko and nimi !="":
        nimi_joukko.add(nimi)
        print("uusi nimi")
    elif nimi in nimi_joukko:
        print("aiemmin syötetty nimi!")
    #print(nimi_joukko)
    nimi = str(input("Anna nimi:"))

for name in nimi_joukko:
    print(name)