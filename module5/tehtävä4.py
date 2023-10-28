'''
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
'''
kaupungit=[]
print("Syötä viiden kaupungin nimet yksi kerrallaan.")
for i in range(1,6):
    kaupungit.append(input(f"Kaupunki {i}: "))
for kaupunki in kaupungit:
    print(kaupunki)
#Mitenhän saan puskettua githubiin jos tiedosto ei muutu, mutta commitin tekstikuvaus muuttuu...
