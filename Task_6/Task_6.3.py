def gallona_litraksi(bensa):
    litra = bensa / 0.264172052
    return litra

gallona = int (input("anna gallonat:"))

while gallona > 0:
    muunnos = gallona_litraksi(gallona)
    print(f"US gal, {muunnos} ")
    gallona = int(input("lopeta syöttämällä -1 tai anna gallonat:"))
print("ohjelma päättynyt")
