# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
# jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä
# kertaa.Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.
def main():
    print("Syötä nimiä yksi nimi kerrallaan. Voit lopettaa nimien syöttämisen syöttämällä tyhjän rivin.")
    name_set = set()
    user_input = "loop"
    while user_input != "":
        user_input = input("")
        if user_input != "" and user_input not in name_set:
            name_set.add(user_input)
            print("Uusi nimi.")
        elif user_input != "" and user_input in name_set:
            print("Aiemmin syötetty nimi.")
    for name in name_set:
        print(name)


main()
