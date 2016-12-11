"""
Opdracht 2 - Levensverwachting

https://dodona.ugent.be/nl/exercises/849566952/
"""


def levensverwachting(geslacht: str, roker: bool, sport: int, alcohol: int,
                      fastfood: bool) -> None:
    """
    Geef de levensverwachting van een persoon op basis van de volgende invoer.

    :param geslacht: Man of Vrouw als string.
    :param roker: Ja of Nee als boolean.
    :param sport: Uren per week aan sport als integer.
    :param alcohol: Glazen alcohol per week als integer.
    :param fastfood: Ja of Nee als boolean.
    """
    # Leeftijd, in het begin is dit 70 jaar.
    leeftijd = 70.0

    # Voeg daar de gelacht jaren erbij.
    leeftijd += verkrijg_geslacht_jaren(geslacht)

    # Voeg daar de rokers jaren erbij.
    leeftijd += verkrijg_roker_jaren(roker)

    # Voeg daar de sport jaaren erbij.
    leeftijd += verkrijg_sport_jaren(sport)

    # Voeg daar de alcohol jaren erbij.
    leeftijd += verkrijg_alcohol_jaren(alcohol)

    # Voeg daar de fastfood jaren erbij.
    leeftijd += verkrijg_fastfood_jaren(fastfood)

    # Geef de leeftijd in het console.
    print(leeftijd)


def verkrijg_geslacht_jaren(geslacht: str) -> int:
    """
    Verkrijg geslacht jaren.

    :param geslacht: Geslacht als string.
    :return: Verkrijg het aantal levensjaren als integer.
    """
    return 4 if geslacht.lower() == 'vrouw' else 0


def verkrijg_roker_jaren(roker: bool) -> int:
    """
    Verkrijg roker jaren.

    :param roker: Roker als boolean.
    :return: Verkrijg het aantal levensjaren als integer.
    """
    return -5 if roker else 5


def verkrijg_sport_jaren(sport: int) -> int:
    """
    Verkrijg sport jaren.

    :param sport: Sport uren als integer.
    :return: Verkrijg het aantal levensjaren als integer.
    """
    return -3 if sport is 0 else sport


def verkrijg_alcohol_jaren(alcohol: int) -> int:
    """
    Verkrijg het aantal alcohol jaren.

    :param alcohol: Het aantal glazen alcohol per week.
    :return: Het aantal alcohol jaren als boolen.
    """
    # Controleer of de persoon nooit alcohol drinkt.
    if alcohol == 0:

        # Geef 2 jaar terug.
        return 2

    # Als de persoon meer dan 7 glazen per week drink.
    elif alcohol > 7:

        # Het aantal glazen extra * 0,5 jaar.
        return -(alcohol - 7) * 0.5

    # Drink de persoon, maar onder de 7 glazen per week.
    else:

        # Komen daar 0 jaren bij.
        return 0


def verkrijg_fastfood_jaren(fastfood: bool) -> int:
    """
    Verkrijg het aantal fastfood jaren.

    :param fastfood: Fastfood als boolean.
    :return: Het aantal fastfood jaren als boolean.
    """
    return 0 if fastfood else 3


def main() -> None:
    """
    Opdracht 2 - Levensverwachting
    """
    # Persoon 1
    levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10,
                      fastfood=True)

    # Persoon 2
    levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5,
                      fastfood=True)

    # Persoon 3
    levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0,
                      fastfood=False)

    # Persoon 4
    levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14,
                      fastfood=True)

    # Persoon 5
    levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4,
                      fastfood=False)


if __name__ == "__main__":
    main()
