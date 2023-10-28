'''
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
'''

fishlength = float(input("Anna kuhan mitta senttimetreinä:"))
if fishlength < 37:
    print(f"Laske kuha veteen. Se on {37 - fishlength} cm alle alamitan.")
