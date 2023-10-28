'''
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
'''
print("Anna tuumat, niin ohjelma muuttaa ne senteiksi. Lopeta ohjelma syöttämällä \n"
          "negatiivinen arvo.")
inch = 0
while inch >= 0:
    try:
        inch = int(input(""))
    except ValueError:
        print("Käytä kokonaislukuja.")
    cm = 2.54 * inch
    if inch >= 0:
        print(f"{inch} in = {cm} cm.")

