import mysql.connector
from flask import Flask, Response
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
db_cursor = connection.cursor()
db_handler = DatabaseHandler(db_cursor)

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/')
def return_links():
    return ("<a href='http://127.0.0.1:3000/kentt%C3%A4/'>Search airports</a></br>"
            "<a href='http://127.0.0.1:3000/alkuluku'>Primes</a>")


@app.route('/kenttä/')
def show_instructions_airport():
    return ("Add ICAO-code after url, like this <a href='http://127.0.0.1:3000/kentt%C3%A4/EFHK'>"
            "example</a>")


@app.route('/alkuluku/')
def show_instructions_prime():
    return ("Add a number after url, like this <a href='http://127.0.0.1:3000/alkuluku/31'>"
            "example</a>")


@app.route('/kenttä/<icao>')
def get_airport_info(icao):
    return search_icao(icao)


@app.route('/alkuluku/<num>')
def is_prime(num):
    return check_if_prime(num)


def errhandler(error):
    if error == "value_error":
        msg = {'msg': "Not a valid number"}
        errcode = 400
        return msg, errcode
    elif error == "type_error":
        msg = {'msg': "ICAO not found"}
        errcode = 400
        return msg, errcode


def make_response(data, boolean):
    data['isPrime'] = boolean
    return Response(response=json.dumps(data), status=200, mimetype='application/json')


def check_if_prime(num):
    # Oma module5/tehtävä3 algoritmi toimii mutta tämä chat-gpt:n on elegantimpi
    try:
        num = int(num)
        response_data = {'Number': num, 'isPrime': 'ImNotSupposedToBeHere'}
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
                return make_response(response_data, False)
            i += 6
    return make_response(response_data, True)


def search_icao(icao):
    query = f"SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
    db_data = db_handler.exec_and_fetchone(query)
    try:
        db_data_json = {'ICAO': icao.upper(), 'Name': db_data[0], 'Municipality': db_data[1]}
        return db_data_json
    except TypeError:
        message, error_code = errhandler("type_error")
        return Response(response=json.dumps(message), status=error_code, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
