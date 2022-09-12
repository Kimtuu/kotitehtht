import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1', # TAI LOCAL HOST
    port=3306,
    database='flight_game',
    user='root',
    password='iinu123',
    autocommit=True
)

def airport_info(gps_code):
    sql = "select name, municipality from airport where gps_code = '\"" + gps_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)




ICAO = input("Hae lentokenttää ICAO-koodilla: ").upper()
while ICAO != "":
    airport_info(ICAO)
    ICAO = input("Hae lentokenttää ICAO-koodilla tai lopeta painamalla enter: ").upper()
