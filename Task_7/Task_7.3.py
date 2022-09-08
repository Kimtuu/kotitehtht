lentokentät = {"EFHK":"Helsinki-Vantaa",
}

user = int(input("1 = hae lentokenttää\n2 = lisää lentokenttä\n3 = lopeta\nvalitse: "))
if user == 1:
    icao_search = str(input("Hae lentokenttää ICAO-koodilla:"))
    if icao_search in lentokentät:
        print(f"")