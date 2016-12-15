"""
Opdracht 1 - Android patroon hacking
"""
import os
from sys import exit


def main() -> None:
    """
    Opdracht 1 - Android patroon hacking
    """
    # Aantal te cracken codes.
    aantal_bestanden = verkrijg_aantal_bestanden()

    # Alle bestandsnamen
    gesture_bestanden = verkrijg_gesture_bestanden(aantal_bestanden)

    # Lege regel
    print("")

    # Gekraakte codes
    patronen = verkrijg_patronen(gesture_bestanden)

    # Toon de patronen
    toon_patronen(patronen)


def verkrijg_patronen(gesture_bestanden: list) -> list:
    """

    :param gesture_bestanden:
    :return:
    """
    # Placeholder voor alle patronen.
    patronen = []

    # Loop door alle opgegeven bestanden heen.
    for bestand in gesture_bestanden:

        # Voeg het patroon toe aan de lijst.
        patronen.append(verkrijg_patroon(bestand))

    # Geef de lijst met patronen terug.
    return patronen


def verkrijg_patroon(bestand: str) -> list:
    """

    :param bestand:
    :return:
    """
    return [1, 3, 4, 5, 7]


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
                rij.append('.')

        # Teken de rij van het patroon in de console.
        print('----- ----- -----')
        print('| ' + ' | | '.join(rij) + ' |')
        print('----- ----- -----')


def verkrijg_gesture_bestanden(aantal_bestanden: int) -> list:
    """
    Verkrijg alle bestanden die gecrackt moeten worden.

    :param aantal_bestanden:
    :return:
    """
    # Hou alle bestanden bij.
    bestanden = []

    # Ga door het aantal op te vragen bestand heen.
    for x in range(0, aantal_bestanden):

        # Voeg het bestand toe aan de lijst.
        bestanden.append(verkijg_gesture_key_bestand(x + 1))

    # Geef de bestanden terug als list.
    return bestanden


def verkrijg_aantal_bestanden() -> int:
    """
    Verkrijg het aantal Android patroon cracks.

    :return: Het aantal op te vragen patroon cracks.
    """
    # Probeer een getal te vragen.
    try:

        # Geef het ingevulde getal terug.
        return int(input("Aantal patroon cracks: "))

    # Is het geen nummer.
    except ValueError:

        # Geef de foutmelding weer.
        print("Het ingevoerde aantal is niet een nummer.")

        # Stop het script.
        exit()


def verkrijg_bestand(vraag: str) -> str:
    """

    :param vraag:
    :return:
    """
    # Vraag het bestandsnaam op.
    bestandsnaam = str(input(vraag))

    # Controleer of het bestand bestaan.
    if os.path.isfile(bestandsnaam):

        # Geef de naam als string terug.
        return bestandsnaam

    # Zo niet.
    else:

        # Geef weer dat het bestand niet bestaat.
        print("Het opgegeven bestand bestaan niet.")

        # Stop het script.
        exit()


def verkijg_gesture_key_bestand(bestandsnummer: int) -> str:
    """
    Verkrijg het pad naar de gesture.key file.

    :return: Het pas naar de gesture.key file als string.
    """
    return verkrijg_bestand(
        "Pad naar gesture bestand {0}: ".format(bestandsnummer))


def verkrijg_sqlite_bestand() -> str:
    """

    :return:
    """
    return verkrijg_bestand("Pad naar sqlite bestand: ")


if __name__ == '__main__':
    main()
