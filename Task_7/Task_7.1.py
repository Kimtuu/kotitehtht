vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int (input("Anna kuukausi numerona:"))

while True:
    if kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
        print(f"kuukausi sijoittuu vuodenaikaan: {vuodenajat[0]}")
        break
    if kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
        print(f"kuukausi sijoittuu vuodenaikaan: {vuodenajat[1]}")
        break
    if kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
        print(f"kuukausi sijoittuu vuodenaikaan: {vuodenajat[2]}")
        break
    if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
        print(f"kuukausi sijoittuu vuodenaikaan: {vuodenajat[3]}")
        break


