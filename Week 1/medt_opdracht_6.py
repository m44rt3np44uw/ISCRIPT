"""
Opdracht 6 - Zweettest

https://dodona.ugent.be/nl/exercises/1173716008/
"""


def main() -> None:
    """
    Opdracht 6 - Zweettest
    """
    # Verkrijg de leeftijd in maanden en de chlorideconcentratie.
    leeftijd_in_maanden, chlorideconcentratie = verkrijg_waarde()

    # Verkrijg de uitslag.
    uitslag = verkrijg_uitslag(leeftijd_in_maanden, chlorideconcentratie)

    # Toon de uitslag in het console.
    print(uitslag)


def verkrijg_waarde() -> tuple:
    """
    Verkrijg de leeftijd en de chlorideconcentratie in mmol/L van de patient.

    :return: tuple met daarin de leeftijd en de gemeten chlorideconcentratie.
    """
    leeftijd = int(input("Leeftijd (maanden): "))
    chlorideconcentratie = int(input("Chlorideconcentratie (mmol/L): "))

    return leeftijd, chlorideconcentratie


def verkrijg_uitslag(leeftijd_in_maanden: int,
                     chlorideconcentratie: int) -> str:
    """
    Verkrijg de bijbehorende uitslag.

    :param leeftijd_in_maanden: de leeftijd in maanden als int.
    :param chlorideconcentratie: de chlorideconcentratie waarde als int.

    :return: de uitslag als string.
    """
    # Alle soorten uitslagen als string.
    soorten_uitslagen = [
        "CF is hoogst onwaarschijnlijk",
        "CF is mogelijk",
        "CF is waarschijnlijk"
    ]

    # chlorideconcentratie groter dan of gelijk aan 60 mmol/L
    if chlorideconcentratie >= 60:
        return soorten_uitslagen[2]

    # Controleer of de patient jonger is of gelijk aan 6 maanden.
    elif leeftijd_in_maanden <= 6:

        # chlorideconcentratie kleiner dan of
        # gelijk aan 29 millimol per liter (mmol/L)
        if chlorideconcentratie <= 29:
            return soorten_uitslagen[0]

        # chlorideconcentratie tussen 30 – 59 mmol/L:
        elif 30 <= chlorideconcentratie <= 59:
            return soorten_uitslagen[1]

    # Voor personen ouder dan 6 maanden
    elif leeftijd_in_maanden > 6:

        # chlorideconcentratie kleiner dan of gelijk aan 39 mmol/L
        if chlorideconcentratie <= 39:
            return soorten_uitslagen[0]

        # chlorideconcentratie tussen 40 – 59 mmol/L
        elif 40 <= chlorideconcentratie <= 59:
            return soorten_uitslagen[1]


if __name__ == '__main__':
    main()
