"""
Opdracht 9 - Loonbrief

https://dodona.ugent.be/nl/exercises/990750894/
"""


def main() -> None:
    """
    Opdracht 9 - Loonbrief
    :return:
    """
    # Verkrijg het startbedrag.
    startbedrag = verkrijg_startbedrag()

    # Verkijg een lijst met lonen.
    lonen = verkrijg_lonen()

    # Verkrijg het gemiddelde loon.
    gemiddelde_loon = verkrijg_gemiddeld_loon(lonen)

    # Geef het antwoord.
    geef_antwoord(startbedrag, lonen, gemiddelde_loon)


def verkrijg_startbedrag() -> int:
    """
    Verkrijg het startbedrag van de werknemers.

    :return: Het startbedrag als integer.
    """
    return int(input("Startbedrag: "))


def verkrijg_lonen() -> list:
    """
    Verkrijg de lonen van de werknemers.

    :return:
    """
    # Een lijst met de lonen.
    lonen = []

    # Zolang de gebruiker werknemers toe wilt voegen.
    while True:

        # Vraag om een invoer.
        invoer = input("Loon werknemer " + str(len(lonen) + 1) + ": ")

        # Controleer of er meer dan 3 werknemers zijn en de invoer niet gelijk
        # is aan het woord stop.
        if len(lonen) > 3 and invoer.lower() == "stop":

            # Stop de loop.
            break

        # Voeg het loon van de werknemer toe aan de lijst.
        lonen.append(int(invoer))

    # Geef de lijst met lonen terug.
    return lonen


def verkrijg_gemiddeld_loon(lonen: list) -> float:
    """
    Verkrijg het gemiddelde loon van elke werknemer.

    :param lonen: Lijst met lonen van alle werknemers.
    :return: Het gemiddelde loon van elke werknemer.
    """
    # Het totaal van de lonen.
    som = sum(lonen)

    # Het aantal werknemers.
    aantal_werknemers = len(lonen)

    # Geef het gemiddelde loon terug.
    return som / aantal_werknemers


def geef_antwoord(startbedrag: int, lonen: list, gemiddelde_loon: float) -> None:
    """
    Geef het antwoord.

    :param startbedrag: het startbedrag als integer.
    :param lonen: de lonen van de werknemers als list.
    :param gemiddelde_loon: het gemiddelde loon als float.
    """
    # Het start bedrag is tot nu toe het totaal loon.
    totaal_loon = startbedrag

    # Ga door elke loon heen.
    for loon in lonen:

        # Tel het loon erbij op.
        totaal_loon = totaal_loon + loon

        # Geef het totaal bedrag weer in de console van elke werknemer.
        print("werknemer #" + str(lonen.index(loon) + 1) + " fluistert €" + str(totaal_loon))

    # Geef het gemiddelde loon.
    print("gemiddeld loon: €" + str("{0:.2f}".format(gemiddelde_loon)))


if __name__ == "__main__":
    main()
