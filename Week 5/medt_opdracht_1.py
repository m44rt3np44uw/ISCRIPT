"""
Opdracht 1 - Forsyth-Edwards notatie

https://dodona.ugent.be/nl/exercises/867899652/
"""


def main() -> None:
    """
    Opdracht 1 - Forsyth-Edwards notatie
    """
    # Bord 1.
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'))

    # Lege rij.
    print()

    # Bord 2.
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))

    # Lege rij.
    print()

    # Bord 3.
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))

    # Lege rij.
    print()

    # Rooster
    rooster = """rnbqkbnr
                 pppppppp
                 ********
                 ********
                 ********
                 ********
                 PPPPPPPP
                 RNBQKBNR"""

    # Bord 4.
    print(grid2fen(rooster))

    # Lege rij.
    print()

    # Bord 5.
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))

    # Lege rij.
    print()

    # Bord 6.
    print(grid2fen(
        fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'),
        '.'))

    # Lege rij.
    print()

    # Bord 7.
    print(grid2fen(
        fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'),
        '+'))


def fen2grid(fen: str, lege_plek="*") -> str:
    """
    Converteer de FEN als string naar een schaakbord grid.

    :param fen: De FEN als string.
    :param lege_plek: Het opvul icoon voor de lege plekken als string.
    :return: Het schaakbord grid als string.
    """
    # Sla het grid op.
    grid = ""

    # Converteer de string in apparte rijen.
    rijen = fen.split("/")

    # Loop door elke rij heen.
    for rij_nummer, rij in enumerate(rijen):

        # Split de rij op in losse karakters.
        karakters = list(rij)

        # Loop door alle karakters heen.
        for karakter in karakters:

            # Controleer of het karakter geen cijfer is.
            if not karakter.isnumeric():

                # Voeg het toe aan de grid.
                grid += karakter

            # Is het wel een nummer?
            else:

                # Loop door alle posities heen.
                for positie in range(0, int(karakter)):

                    # Vul ze aan met de lege plek.
                    grid += lege_plek

        # Controleer of het niet de laatste rij is.
        if rij_nummer is not (len(rijen) - 1):

            # Voeg een nieuwe regel toe.
            grid += "\n"

    # Geef het grid terug.
    return grid


def grid2fen(rooster: str, lege_plek="*") -> str:
    """

    :param rooster:
    :param lege_plek:
    :return:
    """
    # Split de string op in apparte rijen.
    rijen = '\n'.join(rooster.split()).split('\n')

    # FEN
    fen = ""

    # Ga door elke rij heen.
    for rij_nummer, rij in enumerate(rijen):

        # Split de string op in losse karakters
        karakters = list(rij)

        # Het aantal lege plekken.
        aantal_lege_plekken = 0

        # Ga door ieder karakter heen.
        for karakter_nummer, karakter in enumerate(karakters):

            # Controleer of het karakter geen lege plek is.
            if karakter is not lege_plek:

                # Controleer of het aantal lege plekken niet leeg is.
                if aantal_lege_plekken is not 0:

                    # Voeg het aantal lege plekken toe.
                    fen += str(aantal_lege_plekken)

                    # Leeg het aantal lege plekken.
                    aantal_lege_plekken = 0

                # Voeg het karakter toe aan de FEN.
                fen += karakter

            # Gaat het wel om een lege plek.
            else:

                # Tel dan 1 bij het aantal lege plekken op.
                aantal_lege_plekken += 1

            # Controleer of het aantal lege plekken een hele rij is.
            if (karakter_nummer + 1) is len(
                    rij) and aantal_lege_plekken is not 0:

                # Voeg het aantal lege plekken toe aan de FEN.
                fen += str(aantal_lege_plekken)

                # Zet het aantal lege plekke weer op 0.
                aantal_lege_plekken = 0

        # Controleer of het niet de laatste rij is.
        if rij_nummer is not (len(rijen) - 1):

            # Voeg een nieuwe regel toe aan de FEN.
            fen += "/"

    # return karakters
    return fen


if __name__ == "__main__":
    main()
