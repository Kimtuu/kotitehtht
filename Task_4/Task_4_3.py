# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
import math

nbr_str = input("syötä luku:")
nbr_big = -math.inf
nbr_small = math.inf

while nbr_str != '' :
    i = int(nbr_str)
    if i > nbr_big :
        nbr_big = i
    if i < nbr_small :
        nbr_small = i

    nbr_str = input("anna lukuja:")
if nbr_big == math.inf or nbr_small == math.inf :
    print("et ole syöttänyt mitään:( ")
else:
    print(f"suurin luku: {nbr_big}")
    print(f"pienin luku:{nbr_small}")



