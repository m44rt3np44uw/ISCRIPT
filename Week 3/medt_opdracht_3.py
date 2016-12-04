"""
Opdracht 3 - Vigenecodering

https://dodona.ugent.be/nl/exercises/862295437/
"""
import string


def codeer(originele_tekst: str, sleutelwoord: str) -> None:
    """
    Codeer de tekst.

    :param originele_tekst: De originele tekst als string.
    :param sleutelwoord: Het sleutelwoord als string.
    """
    # Het verlengde sleutelwoord
    verlengd_sleutelwoord = verleng_sleutelwoord(sleutelwoord.upper(),
                                                 len(originele_tekst))

    # Toon de versleutelde tekst.
    print(geef_antwoord(originele_tekst, verlengd_sleutelwoord, True))


def decodeer(versleutelde_tekst: str, sleutelwoord: str) -> None:
    """
    Decodeer de tekst.

    :param versleutelde_tekst: De versleutelde tekst als string.
    :param sleutelwoord: De sleutelwoord als string.
    """
    # Het verlengde sleutelwoord
    verlengd_sleutelwoord = verleng_sleutelwoord(sleutelwoord.upper(),
                                                 len(versleutelde_tekst))

    # Toon de originele tekst.
    print(geef_antwoord(versleutelde_tekst, verlengd_sleutelwoord, False))


def verleng_sleutelwoord(sleutelwoord: str, lengte_boodschap: int) -> str:
    """
    Verleng het sleutelwoord zodat de lengte van het sleutelwoord even lang
    is als de lengte van de boodschap.

    :param sleutelwoord: Het sleutelwoord als string.
    :param lengte_boodschap: De lengte van de boodschap als integer.
    :return: Het verlengde sleutelwoord als string.
    """
    # Verdubbelaar
    verdubbelaar, overige_letters = divmod(lengte_boodschap,
                                           len(sleutelwoord))

    # Geef het exacte sleutelwoord terug.
    return (sleutelwoord * verdubbelaar) + sleutelwoord[0:overige_letters]


def geef_antwoord(tekst: str, verlengd_sleutelwoord: str,
                  versleutelen: bool) -> str:
    """
    Geef het antwoord op de versleutelde of de ontsleutelde tekst.

    :param tekst: De tekst waar het om gaat als string.
    :param verlengd_sleutelwoord: Het verlengde sleutelwoord als string.
    :param versleutelen: Of het versleuteld moet worden of niet als boolean.
    :return: De versleutelde of ontsleutelde tekst.
    """
    # Versleutelde tekst
    versleutelde_tekst = ""

    # Loop door elk letter van de originele tekst heen.
    for index, letter_tekst in enumerate(list(tekst)):
        # Verkrijg de letter uit het sleutelwoord.
        letter_sleutelwoord = verlengd_sleutelwoord[index:index + 1]

        # Verkrijg de versleutelde letter.
        versleutelde_letter = geef_letter(letter_tekst,
                                          letter_sleutelwoord, versleutelen)

        # Voeg de letter toe aan de versleutelde tekst.
        versleutelde_tekst += versleutelde_letter

    # Geeft de tekst terug.
    return versleutelde_tekst


def geef_letter(letter_uit_tekst: str, letter_uit_sleutel: str,
                versleutelen: bool) -> str:
    """
    Geef de versleutelde of ontsleutelde letter.

    :param letter_uit_tekst: De letter uit de tekst als string.
    :param letter_uit_sleutel: De letter uit de sleutel als string.
    :param versleutelen: Of het versleuteld moet worden of niet als boolean.
    :return: De versleutelde of ontsleutelde letter.
    """
    # Controleer of het niet een hoofdletter is. Want alleen de hoofdletters
    # moeten versleuteld worden.
    if not letter_uit_tekst.isupper():

        # Geef de letter direct terug.
        return letter_uit_tekst

    # Is het wel een hoofdletter, dan gaan we het versleutelen.
    else:

        # Verkrijg de positie van de letter in het alfabet (A = 0 en Z = 25).
        index_letter_uit_tekst = string.ascii_uppercase.index(
            letter_uit_tekst)

        # Verkrijg de positie van de letter in het alfabet (A = 0 en Z = 25).
        index_letter_uit_sleutel = string.ascii_uppercase.index(
            letter_uit_sleutel)

        # De versleutelde letter positie in het alfabet.
        versleutelde_letter_index = verkrijg_versleutelde_letter_index(
            index_letter_uit_tekst, index_letter_uit_sleutel, versleutelen)

        # Geef de versleutelde letter terug.
        return string.ascii_uppercase[versleutelde_letter_index]


def verkrijg_versleutelde_letter_index(index_letter_uit_tekst: int,
                                       index_letter_uit_sleutel: int,
                                       versleutelen: bool) -> int:
    """
    Verkrijg de index van een versleutelde letter van het alfabet.

    :param index_letter_uit_tekst: De index van een letter uit de
                                   tekst in het alfabet als integer.
    :param index_letter_uit_sleutel: De index van een letter ui het
                                     sleutelwoord in het alfabet als integer.
    :param versleutelen: Of de string versleuteld moet worden of niet
                         als boolean.
    :return: De index van een letter uit het alfabet.
    """
    # Als er niet versleuteld moet worden.
    if not versleutelen:

        # Wordt de index van de letter uit de sleutel negatief.
        index_letter_uit_sleutel = -abs(index_letter_uit_sleutel)

    # Geef de versleutelde letter index terug.
    return (index_letter_uit_tekst + index_letter_uit_sleutel) % 26


def main() -> None:
    """
    Opdracht 3 - Vigenecodering
    """
    # Codeer 1
    codeer("NOBODY EXPECTS THE SPANISH INQUISITION!", "CIRCUS")

    # Decodeer 1
    decodeer("PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!", "CIRCUS")

    # Codeer 2
    codeer("OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!", "ARTHUR")

    # Decodeer 2
    decodeer("OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!", "ARTHUR")


if __name__ == "__main__":
    main()
