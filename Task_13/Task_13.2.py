import flask
import mysql.connector

connect = mysql.connector.connect(
    host='127.0.0.1',  # TAI LOCAL HOST
    port=3306,
    database='flight_game',
    user='root',
    password='iinu123',
    autocommit=True
)

app = flask.Flask(__name__)


@app.route('/airport/<icao>')
def airport_info(icao):
    sql = f"select gps_code, name, municipality from airport where gps_code= '{icao}'; "
    cursor = connect.cursor()
    cursor.execute(sql)
    ans = cursor.fetchall()
    for row in ans:
        send = f"ICAO: {row[0]}, Name: {row[1]}, Municipality:{row[2]}"
        return send


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
