"""
Opdracht 1 - Android patroon hacking
"""
import binascii
import os
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
    Verkrijg een lijst met cijfers die het patroon vormen om de telefoon te
    unlocken.

    :param gesture_bestand: Het pad naar het gesture bestand als string.
    :param sqlite_bestand: Het pad naar de SQLite bestand als string.
    :return: Geef een list terug met de cijfers van het patroon.
    """
    # Verkrijg de gesture hash.
    gesture_hash = verkrijg_gesture_hash(gesture_bestand)

    # Verkrijg het patroon.
    patroon = verkrijg_patroon_vanuit_database(gesture_hash, sqlite_bestand)

    # Sla alleen de cijfers op uit het resultaat.
    alleen_cijfers = []

    # Loop door elke karakter heen in het resultaat.
    for karakter in patroon:

        # Controleer of het een digit is.
        if karakter.isdigit():

            # Voeg het toe aan de lijst als integer.
            alleen_cijfers.append(int(karakter))

    # Geef de lijst terug.
    return alleen_cijfers


def verkrijg_patroon_vanuit_database(gesture: str,
                                     sqlite_bestand) -> str:
    """
    Haal het bijbehorende patroon op uit de batabase aan de hand van de
    opgegeven hash.

    :param gesture: De hash als string.
    :param sqlite_bestand: Het SQLite bestand als string.
    :return: Het patroon als list.
    """
    # Maak een SQLite connectie.
    connectie = sqlite3.connect(sqlite_bestand)

    # Bereid de huidige connectie voor.
    huidige = connectie.cursor()

    # SQL statement
    sql = "SELECT pattern FROM RainbowTable WHERE hash=\"" + gesture + "\""

    # Probeer een execute.
    try:

        # Voer de SELECT statement uit op de database.
        huidige.execute(sql)

    # Het is geen database file.
    except sqlite3.DatabaseError:

        # Sluit het programma af.
        stop_met_melding("Het opgegeven bestand is geen database.")

    # Verkrijg een rij vanuit de database.
    patroon = huidige.fetchone()

    # Sluit de verbinding af.
    huidige.close()

    # Controleer of het patroon niet leeg is.
    if patroon is not None:

        # Geef alleen het eerste patroon terug.
        return patroon[0]

    # Stop het programma.
    stop_met_melding("Er is geen patroon gevonden me de opgegeven hash.")


def verkrijg_gesture_hash(gesture_bestand: str) -> str:
    """
    Verkrijg de hash vanuit het opgegeven bestand.

    :param gesture_bestand: Pad naar het bestand als string.
    :return: De hash als string.
    """
    # Open het opgegeven bestand.
    with open(gesture_bestand, mode='rb') as bestand:

        # Verkrijg de content uit het bestand.
        content = bestand.read()

        # Probeer het bestand te decoderen.
        try:

            # Haal de gesture hash op uit het bestand.
            gesture_hash = binascii.hexlify(content).decode()

            # Controleer de lengte van de hash
            if len(gesture_hash) is 40:

                # Geef de hash terug.
                return gesture_hash

            # Als het geen hash is.
            else:

                # Stop het programma.
                stop_met_melding("Het opgegeven bestand bevat geen hash.")

        # Als het niet werkt.
        except TypeError:

            # Stop het programma.
            stop_met_melding("Het bestand kan niet gedecodeerd worden.")


def toon_patronen(combinaties: list) -> None:
    """
    Toon alle patronen.

    :param combinaties: Een lijst met combinaties als list.
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

    :param aantal_bestanden: Het aantal op te vragen bestanden als integer.
    :return: Een lijst met bestanden als string.
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

        # Stop het programma.
        stop_met_melding("Het ingevoerde aantal is niet een nummer.")


def verkrijg_bestand(vraag: str) -> str:
    """
    Vraag aan de gebruiker een bestand op en controleer of het bestaat.

    :param vraag: De vraag als string.
    :return: Het pad naar het bestand als string.
    """
    # Vraag het bestandsnaam op.
    bestandsnaam = str(input(vraag))

    # Controleer of het bestand bestaan.
    if os.path.isfile(bestandsnaam):

        # Geef de naam als string terug.
        return bestandsnaam

    # Stop het programma.
    stop_met_melding("Het opgegeven bestand bestaat niet.")


def verkijg_gesture_key_bestand(bestandsnummer: int) -> str:
    """
    Verkrijg het pad naar de gesture.key file.

    :return: Het pas naar de gesture.key file als string.
    """
    return verkrijg_bestand(
        "Pad naar gesture bestand {0}: ".format(bestandsnummer))


def verkrijg_sqlite_bestand() -> str:
    """
    Vraag aan de gebruiker het pad naar het SQLite bestand.

    :return: Verkrijg het pad naar het SQLite bestand als string.
    """
    return verkrijg_bestand("Pad naar sqlite bestand: ")


def stop_met_melding(melding: str) -> None:
    """
    Print de opgegeven melding in de console en stop daarna het script.

    :param melding: De melding als string.
    """
    # Toon de melding in de console.
    print(melding)

    # Stop het programma.
    exit()


# Controleer of het script direct aangeroepen wordt.
if __name__ == '__main__':

    # Voer dan de methode main uit.
    main()
