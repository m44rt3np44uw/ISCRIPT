"""
Opdracht 3 - Vigenecodering

https://dodona.ugent.be/nl/exercises/862295437/
"""
import math
import string


def codeer(originele_tekst: str, sleutelwoord: str) -> None:
    """
    Codeer de tekst.

    :param originele_tekst: De originele tekst als string.
    :param sleutelwoord: Het sleutelwoord als string.
    """
    # Voor de zekerheid wordt de sleuteltekst geconverteerd naar hoofdletters
    sleutelwoord = sleutelwoord.upper()

    # Lengte van de originele tekst.
    lengte_originele_tekst = len(originele_tekst)

    # Het verlengde sleutelwoord
    verlengd_sleutelwoord = verleng_sleutelwoord(sleutelwoord,
                                                 lengte_originele_tekst)

    # Toon de versleutelde tekst.
    print(geef_antwoord(originele_tekst, verlengd_sleutelwoord, True))


def decodeer(versleutelde_tekst: str, sleutelwoord: str) -> None:
    """
    Decodeer de tekst.

    :param versleutelde_tekst: De versleutelde tekst als string.
    :param sleutelwoord: De sleutelwoord als string.
    """
    # Voor de zekerheid wordt de sleuteltekst geconverteerd naar hoofdletters
    sleutelwoord = sleutelwoord.upper()

    # Lengte van de versleutelde tekst.
    lengte_versleutelde_tekst = len(versleutelde_tekst)

    # Het verlengde sleutelwoord
    verlengd_sleutelwoord = verleng_sleutelwoord(sleutelwoord,
                                                 lengte_versleutelde_tekst)

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
    # Lengte van het sleutelwoord
    lengte_sleutelwoord = len(sleutelwoord)

    # Verdubbelaar
    verdubbelaar = math.ceil(lengte_boodschap / lengte_sleutelwoord)

    # Verlengt sleutelwoord
    verlengt_sleutelwoord = sleutelwoord * verdubbelaar

    # Geef het exacte sleutelwoord terug.
    return verlengt_sleutelwoord[0:lengte_boodschap]


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

    # Count
    count = 0

    # Loop door elk letter van de originele tekst heen.
    for letter_tekst in list(tekst):
        # Verkrijg de letter uit het sleutelwoord.
        letter_sleutelwoord = verlengd_sleutelwoord[count:count + 1]

        # Verkrijg de versleutelde letter.
        versleutelde_letter = geef_letter(letter_tekst,
                                          letter_sleutelwoord, versleutelen)

        # Voeg de letter toe aan de versleutelde tekst.
        versleutelde_tekst += versleutelde_letter

        # Tel de count op met 1.
        count += 1

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

        # Controleer of we de letter moeten versleutelen.
        if versleutelen:

            # Tel dan de twee indexen bij elkaar op.
            totale_index = index_letter_uit_tekst + index_letter_uit_sleutel

        # Zo niet.
        else:

            # Trek dan de twee indexen van elkaar af.
            totale_index = index_letter_uit_tekst - index_letter_uit_sleutel

        # De versleutelde letter positie in het alfabet.
        versleutelde_letter_index = totale_index % 26

        # Geef de versleutelde letter terug.
        return string.ascii_uppercase[versleutelde_letter_index]


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
