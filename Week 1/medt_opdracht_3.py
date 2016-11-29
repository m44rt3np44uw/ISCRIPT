"""
Opdracht 3 - Poolcoordinaten

https://dodona.ugent.be/nl/exercises/333498206/
"""
from math import atan, pi, sqrt, pow


def verkrijg_straal(x: float, y: float) -> float:
    """
    Bereken de straal door middel van de opgegeven X en Y coordinaten.

    :param x:   X coordinaat als float.
    :param y:   Y coordinaat als float.
    :return:    straal als float.
    """
    return sqrt(pow(x, 2) + pow(y, 2))


def verkrijg_hoek(x: float, y: float) -> float:
    """
    Verkrijg de hoek door middel van de opgegeven X en Y coordinaten.

    :param x:   X coordinaat als float.
    :param y:   Y coordinaat als float.
    :return:    hoek als float.
    """
    if x == 0:
        return pi * 0.5
    else:
        return atan(y / x)


def main() -> None:
    """
    Opdracht 3 - Poolcoordinaten
    """

    # Vraag de X en Y coordinaten aan de gebruiker.
    x = float(input("X: "))
    y = float(input("Y: "))

    # Verkrijg de straal.
    straal = verkrijg_straal(x, y)

    # Verkrijg de hoek.
    hoek = verkrijg_hoek(x, y)

    # Toon de gegevens op het scherm.
    print(straal)
    print(hoek)


if __name__ == '__main__':
    main()
