"""
Opdracht 3 - Nobelprijzen

https://dodona.ugent.be/nl/exercises/1392321201/
"""
import csv


def main() -> None:
    # Zoekresultaat 1
    print(prijzen("medt_opdracht_3_prijzen.csv", prijs="nobelprijs", jaar=1994))

    # Zoekresultaat 2
    # print(prijzen("medt_opdracht_3_prijzen.csv", prijs="nobelprijs", discipline="wiskunde"))

    # Zoekresultaat 3
    # print(prijzen("medt_opdracht_3_prijzen.csv", nationaliteit="bel"))

    # Zoekresultaat 4
    # print(prijzen("medt_opdracht_3_prijzen.csv", discipline="scheikunde", laureaten=3))

    # Zoekresultaat 5
    # print(prijzen("medt_opdracht_3_prijzen.csv", motivering="röntgen", discipline="natuurkunde", nationaliteit="GB"))


def prijzen(prijzen_csv: str, prijs=None, discipline=None, jaar=None,
            nationaliteit=None, laureaten=None, motivering=None) -> list:
    """
    Een methode om een aantal prijzen uit het CSV bestand uit te schrijven
    die voldoen aan een reeks vooropgestelde criteria.

    :param prijzen_csv: De locatie waar het CSV bestand te vinden is als string.
    :param prijs: De nobelprijs, abelprijs of turing award als string.
    :param discipline: In welke categorie de prijs werd uitgereken als string.
    :param jaar: Het jaar wanneer de prijs uitgerijkt werd als interger.
    :param nationaliteit: De nationaliteit van één van der laureaten als string.
    :param laureaten: Het aantal laureaten waaraan de prijs werd uitgereikt
                      is als integer.
    :param motivering: Motivering van de prijs als string.
    :return: De geselecteerde prijzen als list.
    """
    # Geef de prijzen terug
    return []


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
                          list(str(laureaat).split(',')), str(motivering)]

                # Voeg de rij toe.
                alle_prijzen.append(dict(zip(headers, de_rij)))

    # Geef alle prijzen terug.
    return alle_prijzen


def is_prijs(prijs: str, uitreiking: dict) -> bool:
    """
    Controleer of de uitreiking een bepaalde prijs is.

    :param prijs: De prijs als string.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # De prijs in kleine letters.
    prijs = prijs.lower()

    # De uitreiking prijs in kleine letters.
    uitreiking_prijs = uitreiking['prijs'].lower()

    # Controleer of het de opgegeven prijs is.
    return prijs == uitreiking_prijs


def is_discipline(discipline: str, uitreiking: dict) -> bool:
    """
    Controleert of de discipline overeenkomt met de opgegeven uitreiking.

    :param discipline: De discipline als string.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Discipline in kleine letters.
    discipline = discipline.lower()

    # Discipline uit de uitreiking.
    uitreiking_discipline = uitreiking['discipline'].lower()

    # Controleer of het de opgegeven discipline is.
    return discipline == uitreiking_discipline


def is_jaar(jaar: int, uitreiking: dict) -> bool:
    """
    Controleert of de uitreiking in een bepaalt jaar is.

    :param jaar: Jaartal als integer.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Het uitreiking jaartal.
    uitreiking_jaar = uitreiking['jaar']

    # Controleer of het de opgegeven prijs is.
    return jaar == uitreiking_jaar


def is_nationaliteit(nationaliteit: str, uitreiking: dict) -> bool:
    """
    Controleert of 1 of meerdere van de laureaten de opgegeven
    nationaliteit heeft.

    :param nationaliteit: Nationaliteit als string.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    # Laureaten
    laureaten = uitreiking['laureaat']

    # Nationaliteit
    nationaliteit = nationaliteit.upper()

    # Aantal laureaten met dezelfde nationaliteit.
    aantal_laureaten = 0

    # Loop door elke laureaat heen.
    for laureaat in laureaten:

        # Laureaat nationaliteit.
        laureaat_nationaliteit = laureaat.split('(', 2)[1].split(')', 1)[
            0].upper()

        # Controleer of de nationaliteit voorkomt.
        if nationaliteit in laureaat_nationaliteit:

            # Tel het aantal nationaliteiten op.
            aantal_laureaten += 1

    # Geef het antwoord terug.
    return aantal_laureaten > 0


def is_laureaten(aantal_laureaten: int, uitreiking: dict) -> bool:
    """
    Controleert of het aantal opgegeven laureaten overeen komen met de opgeven
    uitreiking.

    :param aantal_laureaten: Het aantal laureaten als integer.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    return aantal_laureaten is len(uitreiking['laureaat'])


def is_motivering(motivering: str, uitreiking: dict) -> bool:
    """
    Controleert of de opgegeven motivering bij de uitreiking hoor door te
    kijken of het erin voor komt.

    :param motivering: Een gedeelte van de motivering als string.
    :param uitreiking: De uitreiking als dictionary.
    :return: True of False op basis van bovenstaande vraag.
    """
    return motivering in uitreiking["motivering"]


if __name__ == "__main__":
    main()
