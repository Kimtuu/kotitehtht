# luodaan tyhjä lista annettavia lukuja varten

luvut = []
#luvut.sort(reverse=True)
luku = (input("Anna ensimmäinen luku tai lopeta painamalla Enter:"))
while luku != "":
    luvut.append(luku)
    luku = (input("Anna seuraava luku tai lopeta painamalla Enter:"))
else:
    luvut.sort(reverse=True)
    print(luvut[0:5])


#toimii vain 1-9 luvuilla, en saanit int toiminnolla toimimaan :(