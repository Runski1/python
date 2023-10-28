'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
'''

def main():
    list=[]
    i = "loop away boii"
    while i == "loop away boii":
        try:
            userinput = input("Anna kokonaisluku")
            if userinput == "":
                i = "loopnomore"
            else:
                list.append(int(userinput))
        except ValueError:
            print("virheellinen luku.")

    print(f"Listan tekijöiden summa on {listsum(list)}")

def listsum(list):
    return sum(list)

main()
