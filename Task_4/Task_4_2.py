##Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
#1tuuma=2.54
#kysytään käyttäjältä tuumat

inches = float (input("anna tuuma(t):"))
#rakennnetaan while loopin sisään säännöt
while inches >=0 :
    cm = inches * 2.54
    print(inches, "inches=", cm, "cm")
    print("voit keskeyttää muuntamisen syöttämällä 0 pienemmän luvun")
    inches = float (input("anna tuuma(t):"))
#while loopin ulkopuolelle mennään kun inches <= 0
print("muuntaminen keskeytetty")


