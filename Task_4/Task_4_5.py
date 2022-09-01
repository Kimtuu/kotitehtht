#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja
#salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

username_input = str
password_input = str

#while
tries = 5

#username_input = str(input("username:"))
#password_input = str(input("Password"))

while tries > 0 :
    username_input = str(input("username:"))
    password_input = str(input("Password"))
    if username_input == "python" and password_input == "rules":
        print("Tervetuloa")
        break
    if username_input != "python" or password_input != "rules":
        print("pääsy evätty")
    tries-=1
if tries == 0 and username_input != "python" or password_input != "rules":
    print("pääsy evätty")

