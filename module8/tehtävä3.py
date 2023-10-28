"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen 
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston 
avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. 
Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
import mysql.connector
from geopy.distance import geodesic
db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="juurimaria",
    database="flight_game",
    autocommit=True
)


def fetch_coordinates(userinput):
    sql = "SELECT airport.latitude_deg, airport.longitude_deg"
    sql += " FROM airport"
    sql += " WHERE airport.ident = '" + userinput + "'"
    # mitä .cursor, .execute ja .fetchall tekee??
    kursori = db_connection.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    airport_coordinates = (result[0])
    kursori.close()
    return airport_coordinates


coordinate_pair = []
for iterator in range(2):
    ICAO = input(f"Anna {iterator + 1}. ICAO-koodi.")
    coordinate_pair.append(fetch_coordinates(ICAO))
# list unpacker
coord1, coord2 = coordinate_pair
# geopy distance calculating function
distance = geodesic(coord1, coord2).kilometers
print(f"etäisyys lentokenttien välillä: {distance:.2f} km.")

if db_connection.is_connected():
    db_connection.close()
