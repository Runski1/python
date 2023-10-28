'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''
print("Syötä lukuja. Lopuksi saat pienimmän ja suurimman luvun.\n"
      "Kun haluat lopettaa lukujen syötön, syötä tyhjä syöte.")
strlen = 1
while strlen > 0:
    try:
        userinput = input("")
        num = float(userinput)
        #ValueError syntyy sekä tyhjällä syötteellä, että esim. kirjainten syöttämisellä.
    except ValueError:
        if userinput == "":
            print(f"Pienin luku: {num_min}\n"
                  f"Suurin luku: {num_max}")
            quit()
        else:
            print("Virheellinen luku")
    strlen = len(userinput)
    #Kiitos Chat-GPT ideasta:
    #Tässä tarkistetaan onko muuttuja olemassa, jos ei, luodaan se ja annetaan arvo.
    #Näin vältetään muuttujaa määritellessä syötettyjen esiarvojen eksyminen tulosteeseen
    try:
        num_min
    except:
        num_min = num
    try:
        num_max
    except:
        num_max = num

    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num

