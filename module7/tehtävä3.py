# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
# uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
# syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy
# ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

def main():
    airport_dictionary = dict()
    looper = "loop"
    while looper == "loop":
        print("Haluatko syöttää vai hakea lentokenttiä? (S/H)\n"
              "Voit lopettaa ohjelman kirjoittamalla lopeta")
        choose_function = input("").lower()
        if choose_function == "s":
            airport_dictionary = airport_inputter(airport_dictionary)
        elif choose_function == "h":
            airport_searcher(airport_dictionary)
        elif choose_function == "lopeta":
            quit()


def airport_inputter(dictionary):
    icao_input = "loop"
    print("Lisää lentokenttä syöttämällä ICAO-koodi. Syötä tyhjä rivi lopettaaksesi lentokenttien syöttämisen.")
    while icao_input != "":
        icao_input = input("ICAO: ")
        if icao_input != "":
            airport_input = input("Lentokentän nimi: ")
            dictionary.update({icao_input: airport_input})
    return dictionary


def airport_searcher(dictionary):
    icao_input = "loop"
    print("Etsi lentokenttää sen ICAO-koodilla:")
    while icao_input != "":
        icao_input = input("ICAO: ")
        try:
            if icao_input != "":
                print(dictionary[icao_input])
            else:
                break
        except KeyError:
            print("Ei löydy.")



main()