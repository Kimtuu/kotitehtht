
##Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
#1tuuma=2.54
#kysytään käyttäjältä tuumat
inches = float (input("anna tuuma(t):"))

while inches >=0 :
    cm = inches * 2.54
    print(inches, "inches=", cm, "cm")
    inches = float (input("anna tuuma(t):"))
print("muuntaminen keskeytetty")


