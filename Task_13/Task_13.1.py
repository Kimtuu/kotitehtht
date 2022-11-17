import flask

app = flask.Flask(__name__)


@app.route('/prime')
def test_prime():
    args = flask.request.args
    number = int(args.get("number"))
    if number > 1:
        for i in range(2, int(number / 2 + 1)):
            if (number % i) == 0:
                tulos = False
                break
        else:
            tulos = True
    else:
        tulos = False

    vastaus = {
        "number": number,
        "isPrime": tulos
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
