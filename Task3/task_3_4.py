#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

year = int (input("anna vuosiluku:"))
if (year % 400 == 0) and (year % 100 == 0) :
    print("kyseessä on karkausvuosi")
elif (year % 4 == 0) and (year % 100 !=0)   :
    print("kyseessä on karkausvuosi")
else:
    print("ei karkausvuosi")

