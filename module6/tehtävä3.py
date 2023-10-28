'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.

    Yksi gallona on 3,785 litraa.
'''

def gallons_to_litres(gallons):
    litres = 3.785 * gallons
    return litres
def main():
    print("Muunna gallonat litroiksi. Kun haluat sulkea ohjelman, syötä negatiivinen gallonamäärä.")
    V_gallon = 0
    while V_gallon >= 0:
        try:
            V_gallon = float(input("Anna gallonamäärä: "))
            if V_gallon >= 0:
                print(f"{V_gallon} gallonaa litroina: {gallons_to_litres(V_gallon):.2f}")
        except ValueError:
            print("Virheellinen gallonamäärä.")
main()
