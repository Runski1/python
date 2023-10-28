'''

Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

'''
sp = input("Kerro BIOLOGINEN sukupuolesi (M/N): ").lower()
if sp != "m" and sp != "n":
    print("Virheellinen sukupuoli.")
    quit()
try:
    hglob = int(input("Kerro hemoglobiiniarvosi (g/l): "))
except ValueError:
    print("Virheellinen hemoglobiiniarvo.")
    quit()
else:
    if sp == "m":
        if int(hglob) < 134:
            hglobstr = "alhainen"
        elif 134 <= int(hglob) <= 195:
            hglobstr = "normaali"
        elif 195 < int(hglob):
            hglobstr = "korkea"
    elif sp == "n":
        if int(hglob) < 117:
            hglobstr = "alhainen"
        elif 117 <= int(hglob) <= 175:
            hglobstr = "normaali"
        elif 175 < int(hglob):
            hglobstr = "korkea"

    print(f"Hemoglobiinisi on {hglobstr}.")



