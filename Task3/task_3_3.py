#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l

gender = input("sukupuolesi (nainen/mies)? ")
hg_value = int(input("hemoglobiinisi (g/l)?"))

if gender == "nainen" :
    if not (5 < hg_value <300) :
        print("virheellinen hg-arvo")
    # testataan naisen ohjearvot
    elif hg_value <= 117:
        print("hg arvo on alhainen ")
    elif hg_value <=175:
        print("hg-arvo normaali")
    else:
        print("hg-arvo on korkea")

elif gender == "mies" :
    #miehen arvot
    if not (5 < hg_value < 300) :
        print("virheellinen hg-arvo")
    elif hg_value <= 134 :
        print("hg-arvo alhainen")
    elif hg_value <= 195 :
        print("hg-arvo normaali")
    else: print("hg-arvo on korkea")



