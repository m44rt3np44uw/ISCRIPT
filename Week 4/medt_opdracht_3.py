"""
Opdracht 3 - Experimentele verjaardagsparadox

https://dodona.ugent.be/nl/exercises/1257408557/
"""
from random import randint
from collections import Counter


def main() -> None:
    """
    Opdracht 3 - Experimentele verjaardagsparadox
    """
    # gebeuren samen
    print(gebeuren_samen(6, 3))
    print(gebeuren_samen(6, 3))

    # Schat kans
    print("%.4f" % schat_kans(6, 2, 10000))
    print("%.4f" % schat_kans(365, 23, 10000))


def gebeuren_samen(aantal_mogelijke_uitkomsten: int,
                   aantal_willekeurige_uikomsten: int) -> bool:
    """
    Een methode die voor een type gebeurtenis met m mogelijke uitkomsten,
    n willekeurige uitkomsten genereert en teruggeeft of er zich minstens
    twee gebeurtenissen met dezelfde uitkomst voordoen.

    :param aantal_mogelijke_uitkomsten: Mogelijke uitkomsten als integer.
    :param aantal_willekeurige_uikomsten: Willekeurige uitkomsten als integer.
    :return: Waar of niet waar op basis van bovenstaande vraag als boolean.
    """
    # Hou alle willekeurige uitkomsten bij.
    willekeurige_uikomsten = []

    # Ga door het aantal willekeurige uitkomsten heen.
    for willekeurige_uikomst in range(0, aantal_willekeurige_uikomsten):
        # Vul de lijst aan met een willekeurig nummer.
        willekeurige_uikomsten.append(randint(1, aantal_mogelijke_uitkomsten))

    # De willekeurige nummers en de aantallen.
    aantallen = Counter(willekeurige_uikomsten)

    # Controleer of er waardes zijn de gelijk zijn.
    return len(list(aantallen.values())) < aantal_willekeurige_uikomsten


def schat_kans(aantal_mogelijke_uitkomsten: int,
               aantal_willekeurige_uikomsten: int,
               aantal_testen: int) -> float:
    """
    een functie die de kans berekent dat er bij nn willekeurige
    gebeurtenissen met mm mogelijke uitkomsten, minstens twee
    gebeurtenissen zijn met dezelfde uitkomst.

    :param aantal_mogelijke_uitkomsten: Mogelijke uitkomsten als integer.
    :param aantal_willekeurige_uikomsten: Willekeurige uitkomsten als integer.
    :param aantal_testen: Het aantal uit te voeren testen als integer.
    :return: De kans als float.
    """
    # Het aantal dubbele uitkomsten gevonden per test.
    aantal_dubbele_uitkomsten = 0

    # Ga door het aantal testen heen.
    for test in range(0, aantal_testen):

        # Conroleer of het mogelijk is dat het een dubbele uitvoer heeft.
        if gebeuren_samen(aantal_mogelijke_uitkomsten,
                          aantal_willekeurige_uikomsten):
            # Tel er 1 bij op.
            aantal_dubbele_uitkomsten += 1

    # Geef de kans terug.
    return float(aantal_dubbele_uitkomsten / aantal_testen)


if __name__ == "__main__":
    main()
