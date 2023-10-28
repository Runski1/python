'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True
'''
print("Anna lukuja. voit lopettaa lukujen antamisen tyhjällä syötteellä.")
x = "luupdiluup"
list = []
while x == "luupdiluup":
    try:
        userinput = input("Anna luku")
        num = float(userinput)
        list.append(num)
    except ValueError:
        if userinput == "":
            x = "No loopdiloop:("
        else:
            print("Virheellinen luku.")
for x in range(5):
    print(sorted(list, reverse=True)[x])



