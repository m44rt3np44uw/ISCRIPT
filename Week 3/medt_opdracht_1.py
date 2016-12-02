"""
Opdracht 1 - Heen en terug

https://dodona.ugent.be/nl/exercises/738605545/
"""


def decodeer(geheime_boodschap: str, aantal_kolommen: int) -> None:
    """
    :param geheime_boodschap: Geheime boodschap als string.
    :param aantal_kolommen: Aantal kolommen als integer.
    """
    # Verkrijg de geheime boodschap als lijst.
    als_lijst = naar_lijst(geheime_boodschap, aantal_kolommen)

    # Geef het antwoord
    geef_antwoord(als_lijst, aantal_kolommen)


def geef_antwoord(geheime_boodschap: list, aantal_kolommen: int) -> None:
    """
    Geef het antwoord.

    :param geheime_boodschap: De geheime boodschap als list.
    :param aantal_kolommen: Aantal kolommen als integer.
    """
    # Aantal rijen.
    aantal_rijen = len(geheime_boodschap)

    # Boodschap
    boodschap = ""

    # Ga door elke kolom heen.
    for kolom_nummer in range(0, aantal_kolommen):

        # Ga door elke rij heen.
        for rij_nummer in range(0, aantal_rijen):
            # Voeg het karakter toe aan het antwoord.
            boodschap += geheime_boodschap[rij_nummer][kolom_nummer]

    # Geef de boodschap weer in de console.
    print(boodschap)


def naar_lijst(geheime_boodschap: str, aantal_kolommen: int) -> list:
    """
    Verkrijg de geheime boodschap als lijst.

    :param geheime_boodschap: De geheime boodschap als string.
    :param aantal_kolommen: Het aantal kolommen als integer.

    :return: De geheime boodschap als lijst.
    """
    # In deze lijst komen alle rijen.
    lijst = []

    # Index voor het controleren voor oneven rijen.
    index = 0

    # Loop door elk stukje van de geheime boodschap heen.
    for start in range(0, len(geheime_boodschap), aantal_kolommen):

        # Sla het stukje boodschap op.
        rij = geheime_boodschap[start:start + aantal_kolommen]

        # Controleer of de rij oneven is.
        if not is_even(index):
            # Draai de volgorde om.
            rij = rij[::-1]

        # Voeg het toe aan de lijst.
        lijst.append(rij)

        # Index
        index += 1

    # Geef de lijst terug.
    return lijst


def is_even(getal: int) -> bool:
    """
    Controleer of het getal even is.

    :param getal: Het getal als integer.
    :return: Antwoord op de vraag als boolean.
    """
    return getal % 2 == 0


def main() -> None:
    """
    Opdracht 1 - Heen en terug
    :return:
    """
    # Boodschap 1
    decodeer("aoesifibolwkrdexeioayngoxxfhtslhtlx", 5)

    # Boodschap 2
    decodeer("aohpdntilirndsnefxxftgonomceexxrloewftmyex", 6)


if __name__ == "__main__":
    main()
