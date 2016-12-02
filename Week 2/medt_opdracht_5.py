"""
Opdracht 5 - Sterke wachtwoorden

https://dodona.ugent.be/nl/exercises/417422714/
"""
import string


def main() -> None:
    """
    Opdracht 5 - Sterke wachtwoorden
    """
    # Verkrijg het aantal wachtwoorden.
    aantal_wachtwoorden = verkrijg_aantal_wachtwoorden()

    # Verkrijg de wachtwoorden.
    wachtwoorden = verkrijg_wachtwoorden(aantal_wachtwoorden)

    # Ga door elk wachtwoord heen.
    for wachtwoord in wachtwoorden:

        # Doe de controle en verkijg het aantal goed gecontroleerde vragen.
        aantal_goed = doe_controle(wachtwoord)

        # Toon het antwoord in de console.
        geef_antwoord(aantal_goed)


def is_minstens_acht_karakters(wachtwoord: str) -> bool:
    """
    Controleert of het wachtwoord minimaal 8 karakters lang is.

    :param wachtwoord: Het wachtwoord als string.
    :return: Antwoord op de bovengestelde vraag als boolean.
    """
    # Geef terug of het wachtwoord langer is dan 8 karakters.
    return len(wachtwoord) > 8


def heeft_minimaal_een_hoofdletter(wachtwoord: str) -> bool:
    """
    Controleert of het wachtwoord minimaal 1 hoofdletter heeft.

    :param wachtwoord: Het opgegeven wachtwoord als string.
    :return: Antwoord op de vraag als boolean.
    """
    # Loop door elk karakter van het wachtwoord heen.
    for karakter in list(wachtwoord):

        # Controleer of het karakter een hoofdletter is.
        if karakter.isupper():

            # Zo ja, geef true terug.
            return True

    # Geen hoofdletters gevonden? geef false terug.
    return False


def heeft_minimaal_een_kleine_letter(wachtwoord: str) -> bool:
    """
    Controleert of het wachtwoord minimaal 1 kleine letter heeft.

    :param wachtwoord: Het opgegeven wachtwoord als string.
    :return: Antwoord op de vraag als boolean.
    """
    # Loop door elk karakter van het wachtwoord heen.
    for karakter in list(wachtwoord):

        # Controleer of het karakter een kleine letter is.
        if karakter.islower():

            # Zo ja, geef true terug.
            return True

    # Geen kleine letters gevonden? geef false terug.
    return False


def heeft_minimaal_een_cijfer(wachtwoord: str) -> bool:
    """
    Controleert of het wachtwoord minimaal 1 cijfer heeft.

    :param wachtwoord: Het opgegeven wachtwoord als string.
    :return: Antwoord op de vraag als boolean.
    """
    # Loop door elk karakter van het wachtwoord heen.
    for karakter in list(wachtwoord):

        # Controleer of het karakter een cijfer is.
        if karakter.isnumeric():

            # Zo ja, geef true terug.
            return True

    # Geen cijfers gevonden? geef false terug.
    return False


def heeft_minimaal_een_speciaal_karakter(wachtwoord: str) -> bool:
    """
    Controleert of het wachtwoord minimaal 1 speciaal karakter heeft.

    :param wachtwoord: Het opgegeven wachtwoord als string.
    :return: Antwoord op de vraag als boolean.
    """
    # Een lijst met speciale karakters
    speciale_karakters = list(string.punctuation)

    # Loop door elk karakter van het wachtwoord heen.
    for karakter in list(wachtwoord):

        # Controleer of het karakter een speciaal karakter is.
        if karakter in speciale_karakters:

            # Zo ja, geef true terug.
            return True

    # Geen speciale karakters gevonden? geef false terug.
    return False


def verkrijg_aantal_wachtwoorden() -> int:
    """
    Vraag het aantal wachtwoorden.

    :return: Het aantal wachtwoorden als integer.
    """
    return int(input("Aantal wachtwoorden: "))


def verkrijg_wachtwoorden(aantal_wachtwoorden: int) -> list:
    """
    Verkrijg de wachtwoorden.

    :param aantal_wachtwoorden: Het aantal gewenste wachtwoorden.
    :return: Een lijst met wachtwoorden.
    """
    # Een lijst met wachtwoorden.
    wachtwoorden = []

    # Vraag de wachtwoorden.
    for wachtwoord_nummer in range(0, aantal_wachtwoorden):

        # Vraag het wachtwoord.
        wachtwoord = input("Wachtwoord " + str(wachtwoord_nummer + 1) + ": ")

        # Voeg het toe aan de lijst.
        wachtwoorden.append(wachtwoord)

    # Geef de lijst met wachtwoorden terug.
    return wachtwoorden


def doe_controle(wachtwoord: str) -> int:
    """
    Controleer elk punt van het wachtwoord.

    :param wachtwoord: Het opgegeven wachtwoord als string.
    :return: Het aantal goed gekeurde controles.
    """
    # Het aantal goed gekeurde controles.
    aantal_controles_goed = 0

    # Controleer of het wachtwoord minstens 8 karakters lang is.
    if is_minstens_acht_karakters(wachtwoord):

        # Verhoog het aantal goede controles.
        aantal_controles_goed += 1

    # Controleer of het minimaal 1 hoofdletter heeft.
    if heeft_minimaal_een_hoofdletter(wachtwoord):

        # Verhoog het aantal goede controles.
        aantal_controles_goed += 1

    # Controleer of het minimaal 1 kleine letter heeft.
    if heeft_minimaal_een_kleine_letter(wachtwoord):

        # Verhoog het aantal goede controles.
        aantal_controles_goed += 1

    # Controleer of het minimaal 1 cijfer heeft.
    if heeft_minimaal_een_cijfer(wachtwoord):

        # Verhoog het aantal goede controles.
        aantal_controles_goed += 1

    # Controleer of het minimaal 1 speciaal karakter heeft.
    if heeft_minimaal_een_speciaal_karakter(wachtwoord):

        # Verhoog het aantal goede controles.
        aantal_controles_goed += 1

    # Geef het aantal goed gecontroleerde vragen terug.
    return aantal_controles_goed


def geef_antwoord(aantal_controles_goed: int) -> None:
    """
    Geef het antwoord op de vraag.

    :param aantal_controles_goed: Het aantal goed gekeurde
           controles als integer.
    """
    # Controleer of het aantal 3 of 4 is.
    if aantal_controles_goed == 3 or aantal_controles_goed == 4:

        # Controle is matig.
        controle = "matig"

    # Controleer of het aantal 5 is.
    elif aantal_controles_goed == 5:

        # Controle is sterk.
        controle = "sterk"

    # Andere uitkomsten.
    else:

        # Controle is zwak.
        controle = "zwak"

    # Print het antwoord in de console.
    print(controle)


if __name__ == "__main__":
    main()
