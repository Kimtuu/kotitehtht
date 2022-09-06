import random

def nopan_heitto(tahko):
    silmäluku = (random.randint(1,tahko))
    return silmäluku

silmäluku = int (input("montako tahkoa nopassa?"))

while True:
    noppa = nopan_heitto(silmäluku)
    print(noppa)
    if noppa == silmäluku:
        break

