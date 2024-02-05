import json

def pridaj_udaje(slovnik, krajina, hlavne_mesto):
    slovnik[krajina] = hlavne_mesto
    print(f"{krajina} s hlavným mestom {hlavne_mesto} bolo pridané.")

def vymaz_udaje(slovnik, krajina):
    if krajina in slovnik:
        del slovnik[krajina]
        print(f"{krajina} bolo odstránené zo záznamov.")
    else:
        print(f"{krajina} nie je v záznamoch.")

def najdi_udaje(slovnik, krajina):
    if krajina in slovnik:
        print(f"Hlavné mesto krajiny {krajina} je {slovnik[krajina]}.")
    else:
        print(f"{krajina} nie je v záznamoch.")

def uprav_udaje(slovnik, krajina, nove_hlavne_mesto):
    if krajina in slovnik:
        slovnik[krajina] = nove_hlavne_mesto
        print(f"Hlavné mesto pre {krajina} bolo aktualizované na {nove_hlavne_mesto}.")
    else:
        print(f"{krajina} nie je v záznamoch.")

def uloz_udaje(slovnik, subor):
    with open(subor, 'w') as f:
        json.dump(slovnik, f)
    print("Údaje boli úspešne uložené do súboru.")

def nacitaj_udaje(subor):
    try:
        with open(subor, 'r') as f:
            slovnik = json.load(f)
        print("Údaje boli úspešne načítané zo súboru.")
        return slovnik
    except FileNotFoundError:
        print("Súbor nebol nájdený. Vytvorený nový prázdny slovník.")
        return {}


krajiny_a_hlavne_mesta = {}

pridaj_udaje(krajiny_a_hlavne_mesta, "Slovensko", "Bratislava")
pridaj_udaje(krajiny_a_hlavne_mesta, "Cesko", "Praha")
pridaj_udaje(krajiny_a_hlavne_mesta, "Rakusko", "Vieden")

vymaz_udaje(krajiny_a_hlavne_mesta, "Rakusko")


najdi_udaje(krajiny_a_hlavne_mesta, "Cesko")

uprav_udaje(krajiny_a_hlavne_mesta, "Slovensko", "Kosice")

uloz_udaje(krajiny_a_hlavne_mesta, "krajiny.json")

nacitaj_udaje("krajiny.json")
