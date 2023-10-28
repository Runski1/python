'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
'''
import random
try:
    dicecount = int(input("Kuinka montaa noppaa heitetään? "))
except ValueError:
    print("Virheellinen luku")
    quit()
roll_total = 0
for i in range(0, dicecount):
    roll = random.randint(0,6)
    print(f"roll {i+1}: {roll}")
    roll_total += roll
print(f"Noppien silmäluku yhteensä: {roll_total}")
