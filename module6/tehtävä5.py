'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
jälkeen sekä alkuperäisen että karsitun listan.
'''
def main():
    list=[]
    print("Syötä kokonaislukuja listaan. Lopeta lukujen syöttäminen syöttämällä tyhjää")
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
    print(list)
    print(only_evens_cheatGPT(list))

def only_evens(list):
    newlist = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            newlist.append(list[i])
    return newlist

#Tämä ehkä vähän "fiksummin"
def only_evens2(list):
    newlist = []
    for number in list:
        if number % 2 == 0:
            newlist.append(number)
    return newlist
#CHAT-GPT koodaa 100 kertaa minua paremmin:
def only_evens_cheatGPT(list):
    newlist = [number for number in list if number % 2 == 0]
    return newlist
main()
