import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',  # TAI LOCAL HOST
    port=3306,
    database='flight_game',
    user='root',
    password='iinu123',
    autocommit=True
)

def cordinate_src(icao_code):
    sql = "select latitude_deg, longtitude_deg from airport where gps_code = '\"" + icao_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao_1 = input("anna 1. lentokentän ICAO-koodi: ")
icao_2 = input("anna 2. lentokentän ICAO-koodi: ")
airport_1 = cordinate_src(icao_1)
airport_2 = cordinate_src(icao_2)

print(f"{distance.distance(airport_1, airport_2).km:.2f}km")