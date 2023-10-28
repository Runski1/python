'''
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota
'''
import math
def main():
    # luodaan pizzalista muotoa [pizza1 halkaisija, pizza1 hinta, pizza2 halkaisija, pizza2 hinta]
    pizzalist = []

    for i in range(2):
        try:
            d = float(input(f"Anna {i + 1}. pizzan halkaisija sentteinä: "))
            price = float(input(f"Anna {i + 1}. pizzan hinta euroina: "))
        except ValueError:
            print("Virheellinen syöte. Ohjelma pysäytetään.")
            quit()
        pizzalist.append(d)
        pizzalist.append(price)
# Taiotaan halvempi hinta funktion palauttamasta listasta
    if pricecompare(pizzalist)[0] > pricecompare(pizzalist)[1]:
        print(f"Toinen pizza on halvempi {pricecompare(pizzalist)[1]:.2f} euron neliöhinnalla.")
    else:
        print(f"Ensimmäinen pizza on halvempi {pricecompare(pizzalist)[0]:.2f} euron neliöhinnalla.")

def pricecompare(list):
    valuelist = []
    # ???
    valuelist.append(list[1] / (math.pi * (list[0] / 200) ** 2))
    valuelist.append(list[3] / (math.pi * (list[2] / 200) ** 2))
    return valuelist
    # profit
main()
