lentokentät = {"EFHK" : "Helsinki-Vantaa"}
user = int(input("1 =hae lentokenttää  2=lisää lentokenttä   3=lopeta  \nvalitse: "))
while user != 3:
    if user == 1:
        icao_search = str(input("Hae lentokenttää ICAO-koodilla: ")).upper()
        if icao_search in lentokentät:
                print(f"Lentokenttä {icao_search} on {lentokentät[icao_search]}")
        elif icao_search not in lentokentät:
            print("Lento kenttää ei ole tietokannassa")
    if user == 2:
        ICAO = str(input("Anna ICAO: ")).upper()
        airport_name = str(input("Lentokentän nimi: "))
        lentokentät[ICAO] = airport_name
    user = int(input("1 =hae lentokenttää  2=lisää lentokenttä   3=lopeta  \nvalitse: "))



print("ohjelma lopetettu")
print(lentokentät)