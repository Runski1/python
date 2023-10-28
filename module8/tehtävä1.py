"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="juurimaria",
    autocommit=True
)


def fetch_airport_name(icaocode):

    sql_input = "SELECT airport.name, airport.municipality "
    sql_input += "FROM airport"
    sql_input += " WHERE airport.ident = '" + icaocode + "'"
    #print(sql_input)
    kursori = connection.cursor()
    kursori.execute(sql_input)
    result = kursori.fetchall()
    if kursori.rowcount > 0:
        for row in result:
            print(row)
    return


icao = input("Anna lentokentän ICAO-koodi: ")
fetch_airport_name(icao)
