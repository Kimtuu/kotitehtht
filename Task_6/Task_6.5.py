import random
import math

def parittomien_poistaja(nro_lista):
    num = 0
    nro_lista_ei_parit = []
    while num < len(nro_lista):
        if nro_lista[num] % 2 == 0:
            nro_lista_ei_parit.append(nro_lista[num])

        num = num + 1

    return nro_lista_ei_parit

if True:
    lista = random.sample(range(1,101),10)
    print(f"alkup. lista:{lista}")
    print(f"Lista ilm. parittomia: {parittomien_poistaja(lista)}")