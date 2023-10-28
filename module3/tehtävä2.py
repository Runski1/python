'''

Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
(LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä ifelse/elif/-toistorakennetta.

    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.

Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
'''
x = 0
while x == 0:
    cabin = (input("Kirjoita hyttiluokkasi (LUX, A, B, C): ")).lower()
    if cabin == "lux":
        print("LUX on parvekkeellinen hytti yläkannella.")
        x = 1
    elif cabin == "a":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
        x = 1
    elif cabin == "b":
        print("B on ikkunaton hytti autokannen yläpuolella.")
        x = 1
    elif cabin == "c":
        print ("C on ikkunaton hytti autokannen alapuolella.")
        x = 1
    else:
        print("Virheellinen hyttiluokka.")