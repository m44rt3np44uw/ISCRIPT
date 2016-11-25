"""
Opdracht 8 - Pythagorese drietallen

https://dodona.ugent.be/nl/exercises/683768040/
"""
import math


def main() -> None:
    """
    Opdracht 8 - Pythagorese drietallen
    """
    # Verkrijg het getal N.
    n = verkijg_n()

    # Lijst met pythagorees getallen.
    pythagorees_drietallen = verkrijg_pythagorees_drietallen(n)

    # Ga door elk pythagorees drietal heen.
    for drietal in pythagorees_drietallen:

        # Toon het op het scherm.
        print(str(drietal))


def verkrijg_pythagorees_drietallen(n: int) -> list:
    """
    Verkrijg een lijst met pythagorees drietallen waarvan de uitkomst gelijk
    is aan het opgegeven getal n.

    :param n: Het opgegeven positieve natuurlijke getal.
    :return: een lijst met pythagorees drietallen.
    """
    # Lijst met alle drietallen.
    drietallen = []

    # Loop door alle X waardes heen.
    for x in range(1, n):

        # X in het kwadraat.
        x2 = math.pow(x, 2)

        # Loop door alle Y waardes heen.
        for y in range(x + 1, n):

            # Y in het kwadraat.
            y2 = math.pow(y, 2)

            # Z in het kwadraat.
            z2 = x2 + y2

            # De wortel van Z in het kwadraat.
            zs = int(math.sqrt(z2))

            # Controleer of de formule klopt.
            if (zs * zs == z2) and (x + y + zs == n):

                # Voeg het toe aan de lijst.
                drietallen.append((x, y, zs))

    # Geef de lijst terug.
    return drietallen


def verkijg_n() -> int:
    """
    Verkrijg het getal N.

    :return: Het getal N als integer.
    """
    return int(input("N: "))

if __name__ == "__main__":
    main()
