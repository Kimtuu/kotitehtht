import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1', # TAI LOCAL HOST
    port=3306,
    database='flight_game',
    user='root',
    password='iinu123',
    autocommit=True
)

def airport_type_search(iso_country):
    sql = "select type, count(type) from airport where iso_country = '\"" + iso_country + "\"' group by type order by count(type) asc;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(i[0], i[1])
    return

maa_tunnus = input("Anna maatunnus:")
while maa_tunnus != "":
    airport_type_search(maa_tunnus)
    maa_tunnus = input("Anna maatunnus tai lopeta painamalla Enter:")

print("Kiitos ja näkemiin")

#valmis, kysyy uudestaan ja hyvästelee lopussa :)