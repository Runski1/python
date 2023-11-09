'''
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat
luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

  Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
    Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
'''
try:
    num = int(input("Anna luku: "))
except ValueError:
    print("Antamasi luku ei ollut kokonaisluku. Ohjelma keskeytyy.")
    quit()
if num == 1 or num <= 0:
        print (f"Luku {num} ei ole alkuluku.")
        quit()

for x in range(2, num):
    if num % x == 0:
        print(f"Luku {num} ei ole alkuluku.\n"
              f"ensimmäinen löytynyt tekijä: {x}")
        quit()

print(f"Luku {num} on alkuluku.")


