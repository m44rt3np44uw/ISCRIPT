"""
Opdracht 2 - Pythagorese drietallen

https://dodona.ugent.be/nl/exercises/683768040/
"""
import math


def main() -> None:
    """
    Opdracht 2 - Pythagorese drietallen
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

    # Loop door alle A waardes heen.
    for a in range(1, n):

        # B in het kwadraat.
        a2 = math.pow(a, 2)

        # Loop door alle B waardes heen.
        for b in range(a, n):

            # B in het kwadraat.
            b2 = math.pow(b, 2)

            # C in het kwadraat.
            c2 = a2 + b2

            # De wortel van C in het kwadraat.
            cs = int(math.sqrt(c2))

            # Controleer of de formule klopt.
            if (cs * cs == c2) and (a + b + cs == n):

                # Voeg het toe aan de lijst.
                drietallen.append((a, b, cs))

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
