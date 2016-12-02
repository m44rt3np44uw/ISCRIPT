"""
Opdracht 2 - Cryptogrammen

https://dodona.ugent.be/nl/exercises/189652425/
"""
import string


def cryptogram(opgave: str, oplossing: str) -> str:
    """
    De eerste string stelt de gegeven tekst voor uit de opgave van een
    cryptogrampuzzel. De tweede string stelt een gedeeltelijke oplossing
    van het cryptogram voor. Hierbij werden sommige voorkomens van letters
    reeds vervangen door hun corresponderende letter. Letters van de
    gedeeltelijke oplossing die nog niet werden vervangen,
    worden aangegeven door een vraagteken (?).

    Deze functie geeft een string terug die zoveel mogelijk vraagtekens
    uit de gedeeltelijke oplossing vervangt door hun corresponderende
    letter (met behoud van hoofdletters en kleine letters), op basis van
    de letters die reeds werden vervangen.

    :param opgave: stelt de gegeven tekst voor uit de opgave van
                   een cryptogrampuzzel als string.
    :param oplossing: stelt een gedeeltelijke oplossing van het
                      cryptogram voor als string.
    :return: geeft een string terug die zoveel mogelijk vraagtekens
    uit de gedeeltelijke oplossing vervangt door hun corresponderende
    letter (met behoud van hoofdletters en kleine letters), op basis van
    de letters die reeds werden vervangen als string.
    """
    # Oplossing als lijst.
    lijst_oplossing = list(oplossing)

    # Opgave als lijst.
    lijst_opgave = list(opgave)

    # Antwoord
    antwoord = ""

    # Beschikbare letters.
    beschikbare_letter = verkrijg_beschikbare_letter(lijst_oplossing,
                                                     lijst_opgave)

    # Een lijst met speciale karakters
    speciale_karakters = list(string.punctuation)

    # Loop door de bestaande oplossing heen.
    for karakter_index, karakter_oplossing in enumerate(lijst_oplossing):

        # Controleer of het geen speciale teken is.
        if karakter_oplossing not in speciale_karakters:

            # Voeg de beschikbare letter toe aan het antwoord.
            antwoord += karakter_oplossing

        # Het karakter is een vraagteken.
        elif karakter_oplossing is "?":

            # Opgave karakter.
            opgave_karakter = lijst_opgave[karakter_index]

            # Kijk of wij het karakter kunnen raden.
            if opgave_karakter.lower() in beschikbare_letter:

                # Controleer of het een hoofdleter is.
                is_hoofdletter = opgave_karakter.isupper()

                # Sla de letter op.
                letter = beschikbare_letter[opgave_karakter.lower()]

                # Ging het om een hoofdletter.
                if is_hoofdletter:

                    # Converteer de letter naar een hoofdletter.
                    letter = letter.upper()

                # Voeg het karakter toe.
                antwoord += letter

            else:
                antwoord += "?"

        # Het karakter is een speciale teken.
        else:

            # Voeg het leesteken toe.
            antwoord += karakter_oplossing

    # Geef het antwoord terug.
    return antwoord


def verkrijg_beschikbare_letter(lijst_oplossing: list,
                                lijst_opgave: list) -> dict:
    """
    Verkrijg alle beschikbare letters door de letters uit de oplossing te
    vergelijken met de letters uit de opgave.

    :param lijst_oplossing: Alle letters uit de oplossing als list.
    :param lijst_opgave: Alle letters uit de opgave als list.
    :return: Een dictionary met welke letter welk is.
    """
    # Letters die we weten.
    beschikbare_letters = {}

    # Loop door elke verkregen letter uit de oplossing heen.
    for index_oplossing, karakter_oplossing in enumerate(lijst_oplossing):

        # Controleer of het een letter is.
        if karakter_oplossing.isalpha():
            # Letter uit de opgave.
            letter_opgave = lijst_opgave[index_oplossing].lower()

            # Letter oplossing.
            letter_oplossing = karakter_oplossing.lower()

            # Voeg de letter toe aan de lijst.
            beschikbare_letters.update({
                letter_opgave: letter_oplossing
            })

    # Geef de beschikbare letters terug.
    return beschikbare_letters


def main() -> None:
    """
    Opdracht 2 - Cryptogrammen
    """
    # Voorbeeld 1
    opgave = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
    oplossing = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
    print(cryptogram(opgave, oplossing))

    # Voorbeeld 2
    opgave = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
    oplossing = '?h? p?n???a? ?rod?ces I???l??.'
    print(cryptogram(opgave, oplossing))

    # Voorbeeld 3
    opgave = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
    oplossing = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
    print(cryptogram(opgave, oplossing))

    # Voorbeeld 4
    opgave = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
    oplossing = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
    print(cryptogram(opgave, oplossing))


if __name__ == "__main__":
    main()
