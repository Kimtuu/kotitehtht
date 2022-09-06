import math
def yksikköhinta_laskuri(pizza_halk_cm,pizza_hinta):
    pizza_alue_cm2 = math.pi / 4 * pizza_halk_cm ** 2
    pizza_alue_m2 = pizza_alue_cm2 * 0.01 * 0.01
    pizza_hinta_m2 = pizza_hinta / pizza_alue_m2
    return pizza_hinta_m2

if True:
    pizza_1_halk_cm = float(input("1.pizzan halkaisija cm:"))
    pizza_1_hinta = float(input("1. pizzan hinta:"))
    pizza_2_halk_cm = float(input("2.pizzan halkaisija cm:"))
    pizza_2_hinta = float(input("2. pizzan hinta:"))

    pizza_1 = yksikköhinta_laskuri(pizza_1_halk_cm,pizza_1_hinta)
    pizza_2 = yksikköhinta_laskuri(pizza_2_halk_cm,pizza_2_hinta)

    if pizza_1 > pizza_2:
        print("2. pizza neliöhinta parempi")
    else:
        print("1. pizza neliöhinta parempi")