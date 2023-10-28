'''
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
'''
import random
num = random.randint(1,10)
arvaus = 0
print("Tässä pelissä sinun pitää arvata kokonaisluku väliltä 1..10")
while arvaus != num:
    try:
        arvaus = int(input("Arvaa luku: "))
        if arvaus < num:
            print("Liian pieni arvaus")
        elif arvaus > num:
            print("Liian suuri arvaus")
        else:
            print("Oikein!")
    except ValueError:
        print("Virheellinen syöte.")

