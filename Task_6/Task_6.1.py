import random
noppa = 1

def nopan_heitto():
    silmäluku = (random.randint(1,6))
    return silmäluku

while noppa != 6:
    noppa = nopan_heitto()
    print(noppa)
    if noppa == 6:
        break

