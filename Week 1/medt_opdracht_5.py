"""
Opdracht 5 - Territoriale wateren

https://dodona.ugent.be/nl/exercises/587558403/
"""
import math


def verkrijg_maritieme_zone(afstand_tot_basislijn: float) -> str:
    """
    Verkrijg de afstand tot de bassislijn als maritieme naam.

    :param afstand_tot_basislijn: afstand tot basislijn in zeemijlen.

    :return: benaming van de maritieme zone.
    """
    if 0.0 <= afstand_tot_basislijn <= 12.0:
        return "territoriale wateren"
    elif 12.0 <= afstand_tot_basislijn <= 24.0:
        return "aansluitende zone"
    elif 24.0 <= afstand_tot_basislijn <= 200.0:
        return "exclusieve economische zone"
    else:
        return "internationale wateren"


def verkrijg_voetpunt(coordinaat_1: tuple, coordinaat_2: tuple,
                      coordinaat_3: tuple) -> tuple:
    """
    Verkrijg de coordinaten van het voetpunt.

    :param coordinaat_1: Coordinaat punt 1 als float.
    :param coordinaat_2: Coordinaat punt 2 als float.
    :param coordinaat_3: Coordinaat punt 3 als float.

    :return: Coordinaat van het voetpunt als float.
    """
    # Splits de coordinaten op.
    x1, y1 = coordinaat_1
    x2, y2 = coordinaat_2
    x3, y3 = coordinaat_3

    # Verkijg u
    u = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / (
    math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # Verkijg Xv en Yv
    xv = x1 + u * (x2 - x1)
    yv = y1 + u * (y2 - y1)

    # Maak een voetpunt coordinaat.
    voetpunt = (xv, yv)

    # Geef het voetpunt terug
    return voetpunt


def verkrijg_euclidische_afstand(xv: float, x3: float, yv: float,
                                 y3: float) -> float:
    """
    Verkrijg de euclidische afstand.

    :param xv: coordinaat Xv als float.
    :param x3: coordinaat X3 als float.
    :param yv: coordinaat Yv als float.
    :param y3: coordinaat Y3 als float.

    :return: euclidische afstand als float.
    """
    return math.sqrt(math.pow(xv - x3, 2) + math.pow(yv - y3, 2))


def toon_informatie(voetpunt: tuple, afstand_in_zeemijlen: float,
                    zone: str) -> None:
    """
    Toon de informatie in het console.

    :param voetpunt: voetpunt als tuple.
    :param afstand_in_zeemijlen: afstand in zeemijlen als float.
    :param zone: zone als string.
    """
    # Splits het voetpunt op.
    xv, yv = voetpunt

    print("voetpunt: (" + str(xv) + ", " + str(yv) + ")")
    print("afstand: " + str(afstand_in_zeemijlen) + " zeemijl")
    print("zone: " + zone)


def verkrijg_coordinaten() -> list:
    """
    Verkrijg de coordinaten.

    :return: lijst met coordinaten.
    """
    # Lijst met getallen.
    getallen = []

    # Vraag het X en het Y coordinaat voor de 3 punten.
    for getal in range(1, 4):
        # X coordinaat.
        x = input("X" + str(getal) + ": ")

        # Y coordinaat.
        y = input("Y" + str(getal) + ": ")

        # Voeg het coordinaat toe aan de lijst.
        getallen.append((float(x), float(y)))

    # Geef de getallen terug.
    return getallen


def main() -> None:
    """
    Opdracht 5 - Territoriale wateren
    """
    # Verkrijg de coordinaten.
    coordinaat_1, coordinaat_2, coordinaat_3 = verkrijg_coordinaten()

    # Splits de coordinaten van punt 3 op.
    x3, y3 = coordinaat_3

    # Verkrijg het voetpunt.
    voetpunt = verkrijg_voetpunt(coordinaat_1, coordinaat_2, coordinaat_3)

    # Splits de coordinaten van het voetpunt op.
    xv, yv = voetpunt

    # Verkrijg de euclidische afstand.
    euclidische_afstand = verkrijg_euclidische_afstand(xv, x3, yv, y3)

    # Verkrijg de zone als string.
    zone = verkrijg_maritieme_zone(euclidische_afstand)

    # Toon de informatie.
    toon_informatie(voetpunt, euclidische_afstand, zone)


if __name__ == '__main__':
    main()
