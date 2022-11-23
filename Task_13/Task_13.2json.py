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
    ans = cursor.fetchone()
    response = {
        "Icao": ans[0],
        "Name": ans[1],
        "Municipality": ans[2]
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
