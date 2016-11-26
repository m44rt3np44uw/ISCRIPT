"""
Opdracht 10 - Palindroomzinnen

https://dodona.ugent.be/nl/exercises/23570674/
"""
import math


def main() -> None:
    """
    Opdracht 10 - Palindroomzinnen
    """
    # Verkrijg het aantal palindroomzinnen
    aantal_palindroomzinnen = verkrijg_aantal_palindroomzinnen()

    # Verkrijg de palindroomzinnen
    palindroomzinnen = verkrijg_palindroomzinnen(aantal_palindroomzinnen)

    # Controleer de zinnen
    antwoorden = controleer_palindroomzinnen(palindroomzinnen)

    # Ga door elk antwoord heen.
    for antwoord in antwoorden:
        geef_antwoord(antwoord)


def verkrijg_aantal_palindroomzinnen() -> int:
    """
    Verkrijg het aantal palindroomzinnen.

    :return: Het aantal palindroomzinnen als integer.
    """
    return int(input("Aantal palindroomzinnen: "))


def verkrijg_palindroomzinnen(aantal_palindroomzinnen: int) -> list:
    """
    Verkrijg de palindroomzinnen.

    :param aantal_palindroomzinnen: Het gewenst aantal palindroomzinnen.
    :return: Een lijst met palindroomzinnen.
    """
    # Palindroomzinnen
    palindroomzinnen = []

    # Verkrijg elke zin.
    for zin in range(0, aantal_palindroomzinnen):
        # Vraag de zin op.
        opgegeven_zin = str(input("Palindroomzin " + str(zin + 1) + ": "))

        # Voeg de zin toe aan de lijst.
        palindroomzinnen.append(opgegeven_zin)

    # Geef de lijst met zinnen terug.
    return palindroomzinnen


def controleer_palindroomzinnen(palindroomzinnen: list) -> list:
    """
    Geef een lijst terug gevuld met booleans die aangeven of het een
    palindroomzin is of niet.

    :param palindroomzinnen: Een lijst met palindroomzinnen.
    :return: Een lijst met booleans.
    """
    # Een lijst met de booleans
    zijn_palindroomzinnen = []

    # Loop door elke zin heen.
    for palindroomzin in palindroomzinnen:
        # Verkrijg de zin als alleen letters.
        alleen_letters = verkijg_letters(palindroomzin.lower())

        # Verkrijg het aantal karakters van de zin.
        aantal_karakters = len(alleen_letters)

        # Verkrijg de helft + 1
        helft_karakters = math.ceil(aantal_karakters / 2)

        # Het eerste gedeelte van de zin.
        eerste_gedeelte = alleen_letters[:helft_karakters]

        # Het laatste gedeelte van de zin.
        laatste_gedeelte = alleen_letters[-helft_karakters:]

        # Het laatste gedeelte van de zin omgedraaid.
        laatste_gedeelte_omgedraaid = laatste_gedeelte[::-1]

        # Voeg het antwoord toe.
        zijn_palindroomzinnen.append(
            eerste_gedeelte == laatste_gedeelte_omgedraaid)

    # Geef de lijst met booleans terug.
    return zijn_palindroomzinnen


def verkijg_letters(palindroomzin: str) -> str:
    """
    Geef alleen de letters terug in een palindroomzin.

    :param palindroomzin: De palindroomzin.
    :return: een palindroomzin als string.
    """
    # De zin.
    zin = ""

    # Ga door elk karakter heen.
    for karakter in palindroomzin:

        # Controleer of het karakter een letter is.
        if karakter.isalpha():
            # Voeg het karakter toe aan de zin.
            zin += karakter

    # Geef het karakter terug.
    return zin


def geef_antwoord(palindroomzin: bool) -> None:
    """
    Geef het antwoord weer in de console.

    :param palindroomzin: palindroomzin als True of False.
    """
    # Standaard zin.
    zin = "palindroomzin"

    # Als het geen palindroomzin is voeg het woord geen ervoor aan toe.
    if not palindroomzin:
        zin = "geen " + zin

    # Geef de zin weer in de console.
    print(zin)


if __name__ == "__main__":
    main()
