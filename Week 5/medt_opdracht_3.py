"""
Opdracht 3 - Nobelprijzen

https://dodona.ugent.be/nl/exercises/1392321201/
"""
import csv


def prijzen(prijzen_csv: str, prijs=None, discipline=None, jaar=None,
            nationaliteit=None, laureaten=None, motivering=None) -> None:
    """
    Een methode om een aantal prijzen uit het CSV bestand uit te schrijven
    die voldoen aan een reeks vooropgestelde criteria.

    :param prijzen_csv: De locatie waar het CSV bestand te vinden
                        is als string.
    :param prijs: De nobelprijs, abelprijs of turing award als string.
    :param discipline: In welke categorie de prijs werd uitgereken als string.
    :param jaar: Het jaar wanneer de prijs uitgerijkt werd als interger.
    :param nationaliteit: De nationaliteit van één van der
                          laureaten als string.
    :param laureaten: Het aantal laureaten waaraan de prijs werd uitgereikt
                      is als integer.
    :param motivering: Motivering van de prijs als string.
    :return: De geselecteerde prijzen als list.
    """
    # Sla alle prijzen op.
    csv_inhoud = verkrijg_csv_inhoud(prijzen_csv)

    # Controleer of de prijs attribuut niet leeg is.
    if prijs is not None:
        # Filter de prijzen op prijs.
        csv_inhoud = is_prijs(prijs, csv_inhoud)

    # Controleer of de discipline attribuut niet leeg is.
    if discipline is not None:
        # Filter de prijzen op discipline.
        csv_inhoud = is_discipline(discipline, csv_inhoud)

    # Controleer of het jaar attribuut niet leeg is.
    if jaar is not None:
        # Filter de prijzen op jaar.
        csv_inhoud = is_jaar(jaar, csv_inhoud)

    # Controleer of het nationaliteit attribuut niet leeg is.
    if nationaliteit is not None:
        # Filter de prijzen op nationaliteit.
        csv_inhoud = is_nationaliteit(nationaliteit, csv_inhoud)

    # Controleer of het laureaten attribuut niet leeg is.
    if laureaten is not None:
        # Filter de prijzen op laureaten.
        csv_inhoud = is_laureaten(laureaten, csv_inhoud)

    # Controleer of het motevering attribuut niet leeg is.
    if motivering is not None:
        # Filter de prijzen op motivering.
        csv_inhoud = is_motivering(motivering, csv_inhoud)

    # Toon de prijzen.
    return toon_prijzen(csv_inhoud)


def toon_prijzen(uitreikingen: list) -> None:
    """
    Toon alle prijzen in de console met een string opmaak.

    :param uitreikingen: Een lijst met de prijzen als dictionary.
    """
    # Loop door elke prijs heen.
    for uitreiking in uitreikingen:
        # Geef de prijs weer in de console.
        print("{} voor de {} ({}): {}".format(

            # De prijs.
            uitreiking['prijs'],

            # De discipline.
            uitreiking['discipline'].capitalize(),

            # Het jaartal.
            uitreiking['jaar'],

            # De lijst met laureaten.
            ', '.join(uitreiking['laureaat'])
        ))


def verkrijg_csv_inhoud(prijzen_csv: str) -> list:
    """
    Verkrijg de inhoud van de CSV bestand.
    :param prijzen_csv: Bestandsnaam als string.
    :return: Een lijst met rijen.
    """
    # Bestand
    alle_prijzen = []

    # De keys voor de dictionaries.
    headers = ['prijs', 'discipline', 'jaar', 'laureaat', 'motivering']

    # Open het bestand.
    with open(prijzen_csv, "rt", encoding="utf=-8") as bestand:

        # Lees het bestand uit.
        reader = csv.reader(bestand, delimiter=';')

        # Ga door elke rij heen.
        for index, rij in enumerate(reader):

            # Controleer of het niet de header rij is.
            if index is not 0:
                # Sla de kolommen op als losse onderdelen.
                prijs, discipline, jaar, laureaat, motivering = tuple(rij)

                # De rij.
                de_rij = [str(prijs), str(discipline), int(jaar),
                          list(str(laureaat).split(', ')), str(motivering)]

                # Voeg de rij toe.
                alle_prijzen.append(dict(zip(headers, de_rij)))

    # Geef alle prijzen terug.
    return alle_prijzen


def is_prijs(prijs: str, uitreikingen: list) -> list:
    """
    Controleer of de uitreikingen een bepaalde prijs is.

    :param prijs: De prijs als string.
    :param uitreikingen: De uitreikingen als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # De lijst met uitreikingen.
    lijst_uitreikingen = []

    # Ga door elke uitreiking heen.
    for uitreiking in uitreikingen:

        # Controleer of de prijs gelijk is.
        if uitreiking['prijs'].lower() == prijs.lower():
            # Voeg de uitreiking toe aan de lijst.
            lijst_uitreikingen.append(uitreiking)

    # Geef de lijst terug.
    return lijst_uitreikingen


def is_discipline(discipline: str, uitreikingen: list) -> list:
    """
    Controleert of de discipline overeenkomt met de opgegeven uitreikingen.

    :param discipline: De discipline als string.
    :param uitreikingen: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Een lijst met alle uitreikingen.
    lijst_uitreikingen = []

    # Loop door alle uitreikingen heen
    for uitreiking in uitreikingen:

        # Als de discipline overeen komt.
        if uitreiking['discipline'].lower() == discipline.lower():
            # Voeg het toe aan de lijst.
            lijst_uitreikingen.append(uitreiking)

    # Geef de lijst met uitreikingen terug.
    return lijst_uitreikingen


def is_jaar(jaar: int, uitreikingen: list) -> list:
    """
    Controleert of de uitreikingeb in een bepaalt jaar is.

    :param jaar: Jaartal als integer.
    :param uitreikingen: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Een lijst met alle uitreikingen.
    lijst_uitreikingen = []

    # Loop door alle uitreikingen heen
    for uitreiking in uitreikingen:

        # Als het jaar overeen komt.
        if int(uitreiking['jaar']) == jaar:
            # Voeg het toe aan de lijst.
            lijst_uitreikingen.append(uitreiking)

    # Geef de lijst met uitreikingen terug.
    return lijst_uitreikingen


def is_nationaliteit(nationaliteit: str, uitreikingen: list) -> list:
    """
    Controleert of 1 of meerdere van de laureaten de opgegeven
    nationaliteit heeft.

    :param nationaliteit: Nationaliteit als string.
    :param uitreikingen: De uitreikingen als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Een lijst met alle uitreikingen.
    lijst_uitreikingen = []

    # Loop door alle uitreikingen heen
    for uitreiking in uitreikingen:

        # Loop door elke laureaat heen.
        for laureaat in uitreiking['laureaat']:

            # Controleer de nationaliteit.
            if "({})".format(nationaliteit.lower()) in laureaat.lower():
                # Voeg het toe aan de lijst.
                lijst_uitreikingen.append(uitreiking)

    # Geef de lijst terug.
    return lijst_uitreikingen


def is_laureaten(aantal_laureaten: int, uitreikingen: list) -> list:
    """
    Controleert of het aantal opgegeven laureaten overeen komen met de opgeven
    uitreiking.

    :param aantal_laureaten: Het aantal laureaten als integer.
    :param uitreikingen: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Een lijst met alle uitreikingen.
    lijst_uitreikingen = []

    # Loop door alle uitreikingen heen
    for uitreiking in uitreikingen:

        # Controleer het aantal laureaten.
        if len(uitreiking['laureaat']) == aantal_laureaten:
            # Voeg het toe aan de lijst.
            lijst_uitreikingen.append(uitreiking)

    # Geef de lijst terug.
    return lijst_uitreikingen


def is_motivering(motivering: str, uitreikingen: list) -> list:
    """
    Controleert of de opgegeven motivering bij de uitreiking hoor door te
    kijken of het erin voor komt.

    :param motivering: Een gedeelte van de motivering als string.
    :param uitreikingen: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Een lijst met alle uitreikingen.
    lijst_uitreikingen = []

    # Loop door alle uitreikingen heen
    for uitreiking in uitreikingen:

        # Controleer of de motivering voorkomt.
        if motivering.lower() in uitreiking['motivering'].lower():
            # Voeg het toe aan de lijst.
            lijst_uitreikingen.append(uitreiking)

    # Geef de lijst terug.
    return lijst_uitreikingen


def main() -> None:
    # Zoekresultaat 1
    prijzen('medt_opdracht_3_prijzen.csv', prijs='nobelprijs', jaar=1994)

    # Lege regel
    print("")

    # Zoekresultaat 2
    prijzen("medt_opdracht_3_prijzen.csv", prijs="nobelprijs",
            discipline="wiskunde")

    # Lege regel
    print("")

    # Zoekresultaat 3
    prijzen("medt_opdracht_3_prijzen.csv", nationaliteit="bel")

    # Lege regel
    print("")

    # Zoekresultaat 4
    prijzen("medt_opdracht_3_prijzen.csv", discipline="scheikunde",
            laureaten=3)

    # Lege regel
    print("")

    # Zoekresultaat 5
    prijzen("medt_opdracht_3_prijzen.csv", motivering="röntgen",
            discipline="natuurkunde", nationaliteit="GB")


if __name__ == "__main__":
    main()
