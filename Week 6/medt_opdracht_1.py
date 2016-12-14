"""
Opdracht 1 - Android patroon hacking
"""


def main() -> None:
    """
    Opdracht 1 - Android patroon hacking
    """
    # Aantal te cracken codes.
    # aantal_bestanden = verkrijg_aantal_bestanden()

    # Alle bestandsnamen
    # gesture_keys = verkrijg_gesture_bestanden(aantal_bestanden)


def toon_patronen(combinaties: list) -> None:
    """
    Toon alle patronen.

    :param combinaties: Een lijstmet combinaties als list.
    """
    # Ga door alle combinaties heen.
    for nummer, combinatie in enumerate(combinaties):

        # Toon het patroon nummer.
        print("Patroon: " + str(nummer + 1))

        # Toon het patroon.
        toon_patroon(combinatie)

        # Lege regel
        print("")


def toon_patroon(combinatie: list) -> None:
    """
    Toon het patroon in de console.

    :param combinatie: De combinatie van het patroon als list.
    """

    # Loop door de rijen heen.
    for y in range(0, 3):

        # Placeholder voor de rij.
        rij = []

        # Loop de posities heen.
        for x in range(0, 3):

            # Verkijg de X / Y positie als index nummer.
            nummer_voor_positie = y * 3 + x

            # Controleer of het index nummer voor komt in de combinatie.
            if nummer_voor_positie in combinatie:

                # Voeg het toe als stap volgorde.
                rij.append(str(combinatie.index(nummer_voor_positie) + 1))

            # Zo niet.
            else:

                # Voeg een punt toe.
                rij.append('-')

        # Teken het patroon in de console.
        print('----- ----- -----')
        print('| ' + ' | | '.join(rij) + ' |')
        print('----- ----- -----')


def verkrijg_gesture_bestanden(aantal_bestanden: int) -> list:
    """
    Verkrijg alle bestanden die gecrackt moeten worden.

    :param aantal_bestanden:
    :return:
    """


def verkrijg_aantal_bestanden() -> int:
    """
    Verkrijg het aantal Android patroon cracks.

    :return: Het aantal op te vragen patroon cracks.
    """
    return int(input("Aantal patroon cracks: "))


def verkijg_gesture_key_bestand() -> str:
    """
    Verkrijg het pad naar de gesture.key file.

    :return: Het pas naar de gesture.key file als string.
    """
    return str(input("Pad naar gesture.key: "))


if __name__ == '__main__':
    main()
