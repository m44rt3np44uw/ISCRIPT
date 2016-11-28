"""
Opdracht 1 - Game of Life

https://dodona.ugent.be/nl/exercises/511272034/
"""


def main() -> None:
    """
    Opdracht 1 - Game of Life
    """
    # Een generatie
    generatie = [[True] + [False] * 7 for _ in range(6)]

    # Toon de generatie
    toon_generatie(generatie)

    # Aantal buren op positie 0,0
    print(aantal_buren(generatie, 0, 0))

    # Aantal buren op positie 1,1
    print(aantal_buren(generatie, 1, 1))

    # Aantal buren op positie 2,2
    print(aantal_buren(generatie, 2, 2))


def toon_generatie(generatie: list) -> None:
    """
    Toon de generatie in de console.

    :param generatie: Een lijst van rijen die een generatie vormen.
    """
    # Loop door elke rij heen.
    for rij in generatie:

        # De geconverteerde rij.
        geconverteerde_rij = []

        # Loop door elke positie heen.
        for positie in rij:

            # Voeg de positie als X of O toe aan de rij.
            geconverteerde_rij.append(verkrijg_toonbare_positie(positie))

        # Toon de rij.
        print(' '.join(geconverteerde_rij))


def aantal_buren(generatie: list, eigen_x: int, eigen_y: int) -> int:
    """
    Verkrijg het aantal buren die gevuld zijn vanuit een opgegeven positie.

    :param generatie: Een generatie als list.
    :param eigen_x: De X positie als integer.
    :param eigen_y: De Y positie als integer.
    :return: Het aantal buren als integer.
    """
    # De nieuwe X waarde.
    nieuwe_x = eigen_x - 1

    # De nieuwe Y waarde.
    nieuwe_y = eigen_y - 1

    # Aantal buren.
    buren = 0

    # Ga door elke rij heen.
    for x in range(nieuwe_x, nieuwe_x + 3):

        # Ga door elke kolom heen.
        for y in range(nieuwe_y, nieuwe_y + 3):

            # Controleer of die spot gevuld is.
            if generatie[x][y]:

                # Controleert of het niet zijn eigen positie is.
                if not is_eigen_positie((eigen_x, eigen_y), (x, y)):

                    # Controleert of het niet negatief is.
                    if not is_negatief_coordinaat(x, y):

                        # Zo ja, tel 1 buur erbij op.
                        buren += 1

    # Geef het aantal buren terug.
    return buren


def volgende_generatie(generatie: list) -> list:
    """
    Verkrijg de volgende generatie op basis van de spelregels.

    :param generatie: Een lijst van rijen die een generatie vormen.
    :return: Een lijst van rijen die de nieuwe generatie vormen.
    """


def verkrijg_toonbare_positie(bezet: bool) -> str:
    """
    Converteer de positie naar een leesbare boolean.

    :param bezet: Of de positie bezet is of niet als boolean.
    :return: De boolean als string.
    """
    return 'X' if bezet else 'O'


def is_negatief_coordinaat(x: int, y: int) -> bool:
    """
    Controleer of het coordinaat negatief is.

    :param x: X positie als integer.
    :param y: Y positie als integer.
    :return: True of False op basis van een negatief coordinaat.
    """
    return x < 0 or y < 0


def is_eigen_positie(eigen_coordinaat: tuple, opgegeven_coordinaat: tuple) -> bool:
    """
    Controleert of de opgegeven coordinaat niet zijn eigen coordinaat is.

    :param eigen_coordinaat: Eigen coordinaat als list.
    :param opgegeven_coordinaat: Opgegeven coordinaat als list.
    :return: True of False als het opgegeven coordinaat hetzelfde is.
    """
    return eigen_coordinaat == opgegeven_coordinaat

if __name__ == "__main__":
    main()
