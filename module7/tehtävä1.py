
# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
# vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
# monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu
# on ensimmäinen talvikuukausi.
# Tässä ei ole juuri järkeä tallentaa kuukausien nimiä tupleen jos niitä ei tarvitse tehtävässä.
# Kysyn siis käyttäjältä kuukauden nimeä
def main():
    months = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu",
              "lokakuu", "marraskuu", "joulukuu")
    seasons = ("talvikuukasi", "kevätkuukausi", "kesäkuukausi", "syyskuukausi")
    print("Valitse monesko kuukausi:")
    while 0 == 0:
        try:
            month = int(input(""))
            break
        except ValueError:
            print("Virheellinen kuukausi.")

    if month - 1 == 11 or month - 1 <= 1:
        print(f"{months[month-1]} on {seasons[0]}.")
    elif 2 <= month - 1 <= 4:
        print(f"{months[month-1]} on {seasons[1]}.")
    elif 5 <= month - 1 <= 7:
        print(f"{months[month-1]} on {seasons[2]}.")
    elif 8 <= month - 1 <= 10:
        print(f"{months[month-1]} on {seasons[3]}.")


main()
