'''
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko
annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
'''
try:
    year = int(input("Anna vuosiluku: "))
except ValueError:
    print("Virheellinen vuosiluku.")
    quit()
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f"Vuosi {year} ei ole karkausvuosi.")
    else:
        print(f"Vuosi {year} on karkausvuosi.")
else:
    print(f"Vuosi {year} ei ole karkausvuosi.")
