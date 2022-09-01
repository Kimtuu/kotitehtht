#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
#Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import math
import random

arvattu_luku = int
arvottu_luku = random.randint(1, 10)

while arvattu_luku != arvottu_luku:
    arvattu_luku = int(input("arvaa lukua väliltä 1-10:"))
    if arvattu_luku < arvottu_luku :
        print("Liian pieni arvaus")
    elif arvattu_luku > arvottu_luku:
        print("Liian iso arvaus")
    else:
        print("oikein")
        break