'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
'''
pwd = "rules"
username = "python"
try:
i = 0
while i < 5:
    usern = input("Käyttäjätunnus: ")
    passw = input("Salasana: ")
    if usern == username and passw == pwd:
        print("Tervetuloa!")
        quit()
    else:
        i += 1

print("Pääsy evätty.")
except:
    print("Tapahtui odottamaton virhe, jota en jaksa määritellä.")
