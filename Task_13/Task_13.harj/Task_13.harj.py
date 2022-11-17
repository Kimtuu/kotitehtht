from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2
    # return str(summa)

    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa
    }

    json_data = json.dumps(vastaus, default=lambda o: o.__dict__, indent=4)

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
