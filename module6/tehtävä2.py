'''
Muokkaa tehtävä1 siten, että voidaan heittää x-tahkoista noppaa, ja x inputtina funktioon
'''
import random


def dice_throw(sides):
    return random.randint(1, sides)

def main():
    try:
        sides = int(input("Kuinka monta tahkoa nopalle?"))
        throw = 0
        throwcount = 1
        while throw != sides:
            throw = dice_throw(sides)
            print(f"{throw}, {throwcount}")
            throwcount += 1
    except ValueError:
        print("käytä kokonaislukua.")
main()

