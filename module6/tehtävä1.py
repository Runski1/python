'''
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''
import random

def dice_throw():
    return random.randint(1,6)
def main():
    throw = 0
    while throw != 6:
        throw = dice_throw()
        print(throw)

main()
