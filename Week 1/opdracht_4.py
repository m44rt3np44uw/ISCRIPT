"""
Opdracht 4 - Paardensprong

https://dodona.ugent.be/nl/exercises/56374393/
"""
import string


def main() -> None:
    """
    Opdracht 4 - Paardensprong
    """
    # Verkrijg de begin en eind positie.
    (positie_1, positie_2) = verkrijg_posities()

    # Verkrijg alle mogelijke stappen vanuit de begin positie.
    mogelijk = bereken_stap(positie_1, positie_2)

    # Toon de informatie.
    geef_informatie(positie_1, positie_2, mogelijk)


def bereken_stap(positie_1, positie_2) -> bool:
    """
    Bereken of de stap gemaakt kan worden.

    :param positie_1: beginpositie.
    :param positie_2: eindpositie.
    :return: boolean of het kan of niet.
    """
    # Converteer de opgegeven posities naar een array.
    positie_1 = list(positie_1)
    positie_2 = list(positie_2)

    # Split de opgegeven posities op.
    positie_1_letter, positie_1_cijfer = positie_1
    positie_2_letter, positie_2_cijfer = positie_2

    # Letters als index.
    positie_1_letter_index = int(
        string.ascii_lowercase.index(positie_1_letter.lower()) + 1)
    positie_2_letter_index = int(
        string.ascii_lowercase.index(positie_2_letter.lower()) + 1)

    # Alle mogelijke sprongen.
    sprongen = paarden_sprong(int(positie_1_letter_index),
                              int(positie_1_cijfer))

    # Kan de sprong gemaakt worden.
    return (positie_2_letter_index, int(positie_2_cijfer)) in sprongen


def paarden_sprong(x, y):
    """
    Verkrijg elk mogelijke paarden sprong.

    :param x: X positie van de beginstap.
    :param y: Y positie van de beginstap.

    :return: lijst met mogelijke stappen.
    """
    # Verschillende posities.
    verschillende_positites = []

    # Alle mogelijke stappen als offsets.
    stappen_offset = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

    # Controleer elke stap.
    for stap in stappen_offset:

        # Nieuwe X en Y coordinaat.
        nieuw_x = x + stap[0]
        nieuw_y = y + stap[1]

        # Controleer of het niet buiten het veld valt.
        if nieuw_x >= 9 or nieuw_x < 1 or nieuw_y >= 9 or nieuw_y < 1:
            continue

        # Voeg het toe aan de lijst.
        else:
            verschillende_positites.append((nieuw_x, nieuw_y))

    # Geef de lijst terug.
    return verschillende_positites


def geef_informatie(positie_1: str, positie_2: str, kan: bool) -> None:
    """
    Geef de informatie string.

    :param positie_1: positie 1 als string.
    :param positie_2: positie 2 als string.
    :param kan: boolean of het kan of niet.
    """
    print('het paard kan{} springen van {} naar {}'.format(
            [' niet', ''][kan], positie_1, positie_2))


def verkrijg_posities() -> (str, str):
    """
    Verkrijg het startpunt en het gewenste eindpunt van het paard.

    :return: de posities als lijst.
    """
    positie_1 = input("Startpunt : ")
    positie_2 = input("Eindpunt  : ")

    return positie_1, positie_2


if __name__ == '__main__':
    main()
