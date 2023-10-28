'''
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
'''
x = 1
while x <= 1000:
    if x % 3 == 0:
        print(x)
    x += 1
#hyvä kikka
iterator = 3
while iterator <= 1000:
    print(iterator)
    iterator += 3