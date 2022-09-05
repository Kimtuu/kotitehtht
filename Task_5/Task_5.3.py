#alkuluki tehtävä

numero = int (input("Anna tarkastettava numero:"))

if numero > 1:
    for i in range(2,int(numero/2+1)):
        if (numero % i) == 0:
            print(numero, "ei ole alkunumero")
            break
    else:
        print(numero, "on alkunumero")
else:
    print(numero, "ei ole alkunumero")