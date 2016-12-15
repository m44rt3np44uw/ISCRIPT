"""
Opdracht 1 - Android patroon hacking
"""
import binascii
import os
import re
import sqlite3
from sys import exit


def main() -> None:
    """
    Opdracht 1 - Android patroon hacking
    """
    # Aantal te cracken codes.
    aantal_bestanden = verkrijg_aantal_bestanden()

    # Alle bestandsnamen.
    gesture_bestanden = verkrijg_gesture_bestanden(aantal_bestanden)

    # SQLite bestand.
    sqlite_bestand = verkrijg_sqlite_bestand()

    # Lege regel.
    print("")

    # Gekraakte codes.
    patronen = verkrijg_patronen(gesture_bestanden, sqlite_bestand)

    # Toon de patronen.
    toon_patronen(patronen)


def verkrijg_patronen(gesture_bestanden: list, sqlite_bestand: str) -> list:
    """
    Verkrijg van elk opgegeven bestand in de list het bijbehorende patroon
    als list.

    :param: gesture_bestanden: Een lijst met bestanden als list.
    :param: sqlite_bestand: Een SQLite bestand als string.
    :return: Een lijst met patronen als list.
    """
    # Placeholder voor alle patronen.
    patronen = []

    # Loop door alle opgegeven bestanden heen.
    for bestand in gesture_bestanden:

        # Voeg het patroon toe aan de lijst.
        patronen.append(verkrijg_patroon(bestand, sqlite_bestand))

    # Geef de lijst met patronen terug.
    return patronen


def verkrijg_patroon(gesture_bestand: str, sqlite_bestand: str) -> list:
    """

    :param gesture_bestand:
    :return:
    """
    # Verkrijg de gesture hash.
    gesture_hash = verkrijg_gesture_hash(gesture_bestand)

    # Verkrijg het patroon.
    patroon = verkrijg_patroon_vanuit_database(gesture_hash, sqlite_bestand)

    alleen_cijfers = []

    for karakter in patroon:

        if karakter.isnumeric():

            alleen_cijfers.append(int(karakter))

    return alleen_cijfers


def verkrijg_patroon_vanuit_database(gesture_hash: str, sqlite_bestand) -> str:
    """

    :param gesture_hash:
    :return:
    """
    # Maak een SQLite connectie.
    connectie = sqlite3.connect(sqlite_bestand)

    # Bereid de huidige connectie voor.
    huidige = connectie.cursor()

    # Voer de SELECT statement uit op de database.
    huidige.execute("SELECT pattern FROM RainbowTable WHERE hash=\"" + gesture_hash + "\"")

    # Verkrijg een rij vanuit de database.
    patroon = huidige.fetchone()

    # Sluit de verbinding af.
    huidige.close()

    # Controleer of het patroon niet leeg is.
    if patroon is not None:

        # Geef alleen het eerste patroon terug.
        return patroon[0]

    # Is er geen patroon gevonden.
    else:

        # Geef dit terug aan de gebruiker.
        print("Er is geen patroon gevonden me de opgegeven hash.")

        # Sluit het python script af.
        exit()


def verkrijg_gesture_hash(gesture_bestand: str) -> str:
    """

    :param gesture_bestand:
    :return:
    """
    # Open het opgegeven bestand.
    with open(gesture_bestand, mode='rb') as bestand:

        # Verkrijg de content uit het bestand.
        content = bestand.read()

        # Haal de gesture hash op uit het bestand.
        gesture_hash = binascii.hexlify(content).decode()

        # Geef de gesture hash terug.
        return gesture_hash


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
    # # Probeer een getal te vragen.
    # try:
    #
    #     # Geef het ingevulde getal terug.
    #     return int(input("Aantal patroon cracks: "))
    #
    # # Is het geen nummer.
    # except ValueError:
    #
    #     # Geef de foutmelding weer.
    #     print("Het ingevoerde aantal is niet een nummer.")
    #
    #     # Stop het script.
    #     exit()

    # TODO
    return 1


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
    # return verkrijg_bestand(
    #     "Pad naar gesture bestand {0}: ".format(bestandsnummer))

    # TODO
    return "/Users/maartenpaauw/Code/School/Periode 2/ISCRIPT/Week 6/gestures/medt_opdracht_1_gesture_1.key"


def verkrijg_sqlite_bestand() -> str:
    """

    :return:
    """
    # return verkrijg_bestand("Pad naar sqlite bestand: ")

    # TODO
    return "/Users/maartenpaauw/Code/School/Periode 2/ISCRIPT/Week 6/medt_opdracht_1_android_lockscreen_rainbow.sqlite"


if __name__ == '__main__':
    main()
