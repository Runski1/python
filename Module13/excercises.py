import mysql.connector
from flask import Flask, abort, Response
import json


class DatabaseHandler:
    def __init__(self, cursor):
        self.cursor = cursor

    def exec_and_fetchone(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='game',
    password='pass',
    autocommit=True
)
cursor = connection.cursor()
db_handler = DatabaseHandler(cursor)

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/kenttä/<icao>')
def get_airport_info(icao):
    query = f"SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
    db_data = db_handler.exec_and_fetchone(query)
    try:
        db_data_json = {'ICAO': icao.upper(), 'Name': db_data[0], 'Municipality': db_data[1]}
        return db_data_json
    except TypeError:
        abort(404)


@app.route('/alkuluku/<num>')
def is_prime(num):
    # Oma module5/tehtävä3 algoritmi toimii mutta tämä chat-gpt:n on elegantimpi
    try:
        num = int(num)
        response_data = {'Number': num, 'isPrime': 'sad'}
    except ValueError:
        message, error_code = errhandler("value_error")
        return Response(response=json.dumps(message), status=error_code, mimetype='application/json')
    if num <= 2:
        return make_response(response_data, False)
    elif num <= 3:
        return make_response(response_data, True)
    elif num % 2 == 0 or num % 3 == 0:
        return make_response(response_data, False)
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return make_response(response_data, 'sadge')
            i += 6
    return make_response(response_data, True)


def errhandler(error):
    if error == "value_error":
        msg = {'msg': "Not a valid number"}
        errcode = 400
        return msg, errcode


def make_response(data, boolean):
    data['isPrime'] = boolean
    return Response(response=json.dumps(data), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
