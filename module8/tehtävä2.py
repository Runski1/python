""" Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttienlukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne. """

import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="juurimaria",
    database="flight_game",
    autocommit=True
)


def fetch_airport_name(userinput):
    sql = "SELECT airport.type, COUNT(*)"
    sql += "FROM airport"
    sql += " WHERE airport.iso_country = '" + userinput + "'"
    sql += " GROUP BY airport.type;"
    # print(sql)
    # mitä .cursor, .execute ja .fetchall tekee
    kursori = db_connection.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    if kursori.rowcount > 0:
        for row in result:
            print(row)
    return


user_input = input("Anna maakoodi (esim FI): ")
fetch_airport_name(user_input)
