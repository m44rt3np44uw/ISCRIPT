"""
Opdracht 6 - Rorschachtest

https://dodona.ugent.be/nl/exercises/695254392/
"""


def main() -> None:
    """
    Opdracht 6 - Rorschachtest
    """
    # Verkrijg het patroon
    patroon = verkrijg_patroon()

    # Toon de Rorschachtest
    toon_rorschachtest(patroon)


def verkrijg_patroon() -> list:
    """
    Verkrijg het patroon.

    :return: Het patroon als list met elke regel appart.
    """
    # Een lijst met het patroon.
    patroon = []

    # Loop.
    while True:

        # Verkrijg de invoer.
        invoer = str(input())

        # Zolang er geen lege regel gevonden is.
        if invoer == "":
            break

        # Voeg de invoer toe aan de lijst.
        patroon.append(invoer)

    # Geef de invoer terug.
    return patroon


def toon_rorschachtest(patroon: list) -> None:
    """
    Toon het Rorschachtest patroon.

    :param patroon: Het patroon met elke regel in een lijst.
    """
    # Loop door elke regel heen.
    for regel in patroon:

        # Print de regel + de regel in spiegelbeeld.
        print(regel + regel[::-1])


if __name__ == "__main__":
    main()
