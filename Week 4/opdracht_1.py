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

    # Lege regel
    print("")

    # Aantal buren op positie 0,0
    print(aantal_buren(generatie, 0, 0))

    # Aantal buren op positie 1,1
    print(aantal_buren(generatie, 1, 1))

    # Aantal buren op positie 2,2
    print(aantal_buren(generatie, 2, 2))

    # Lege regel
    print("")

    # Toon een aantal volgende generaties.
    for generatie_stap in range(1, 6):

        # Voor de duidelijkheid de generatiestap.
        print("Generatie: ", generatie_stap)

        # Toon de generatie.
        toon_generatie(generatie)

        # Voor de duidelijkheid een lege regel.
        print("")

        # Vernieuw de generatie.
        generatie = volgende_generatie(generatie)


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
    for y in range(nieuwe_y, nieuwe_y + 3):

        # Ga door elke kolom heen.
        for x in range(nieuwe_x, nieuwe_x + 3):

            # Controleert of het niet negatief is.
            if not is_negatief_coordinaat(x, y):

                # Controleer of het niet buiten het veld ligt.
                if not is_buiten_veld(generatie, x, y):

                    # Controleer of die spot gevuld is.
                    if generatie[y][x]:

                        # Controleert of het niet zijn eigen positie is.
                        if not is_eigen_positie((eigen_x, eigen_y), (x, y)):

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
    # De nieuwe generatie.
    nieuwe_generatie = []

    # Loop door elke rij heen.
    for y, rij in enumerate(generatie):

        # Maak de nieuwe rij aan.
        nieuwe_rij = []

        # Loop door elke cel heen.
        for x, cel in enumerate(rij):

            # Sla de nieuwe cel op op basis val spelregel 1.
            nieuwe_cel = spelregel_1(cel, aantal_buren(generatie, x, y))

            # Sla de nieuwe cel op op basis val spelregel 2.
            if not nieuwe_cel:

                # Sla de nieuwe cel op op basis val spelregel 2.
                nieuwe_cel = spelregel_2(cel, aantal_buren(generatie, x, y))

            # Sla de nieuwe cel op op basis val spelregel 3.
            if not nieuwe_cel:

                # Sla de nieuwe cel op op basis val spelregel 3.
                nieuwe_cel = spelregel_3(cel, aantal_buren(generatie, x, y))

            # Voeg de nieuwe cel toe aan de rij.
            nieuwe_rij.append(nieuwe_cel)

        # Voeg de nieuwe rij toe aan de generatie.
        nieuwe_generatie.append(nieuwe_rij)

    # Geef de nieuwe generatie terug.
    return nieuwe_generatie


def spelregel_1(levend: bool, aantal_buurcellen: int) -> bool:
    """
    Als een levende cel door 2 of 3 levende buurcellen omgeven wordt,
    blijft deze cel ook in de volgende generatie levend.

    :param levend: Of de opgegeven cel levend is of niet als boolean.
    :param aantal_buurcellen: Het aantal buurcellen als integer.
    :return: Of de cel blijft leven of niet aan de hand van de bovengestelde
             vraag als boolean.
    """
    return levend and aantal_buurcellen in [2, 3]


def spelregel_2(levend: bool, aantal_buurcellen: int) -> bool:
    """
    Als een levende cel door 4 of meer levende buurcellen omgeven wordt,
    dan gaat deze cel dood door overbevolking. Als een levende cel door
     minder dan twee levende buurcellen omgeven wordt, gaat deze cel
    ook dood, maar dan door eenzaamheid.

    :param levend: Of de opgegeven cel levend is of niet als boolean.
    :param aantal_buurcellen: Het aantal buurcellen als integer.
    :return: Of de cel blijft leven of niet aan de hand van de bovengestelde
             vraag als boolean.
    """
    return levend and aantal_buurcellen in [2, 3]


def spelregel_3(levend: bool, aantal_buurcellen: int) -> bool:
    """
    Als een dode cel wordt omgeven door precies 3 levende buurcellen,
    dan wordt deze dode cel in de volgende generatie levend

    :param levend: Of de opgegeven cel levend is of niet als boolean.
    :param aantal_buurcellen: Het aantal buurcellen als integer.
    :return: Of de cel blijft leven of niet aan de hand van de bovengestelde
             vraag als boolean.
    """
    return not levend and aantal_buurcellen is 3


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


def is_buiten_veld(generatie: list, x: int, y: int) -> bool:
    """
    Controleer of het coordinaat zich buiten het speelveld bevind.

    :param generatie: De huidige generatie als list.
    :param x: Het X coordinaat als integer.
    :param y: Het Y coordinaat als integer.
    :return: True of False op basis van bovenstaande vraag.
    """
    lengte_x = len(generatie[0]) - 1
    lengte_y = len(generatie) - 1

    return x > lengte_x or y > lengte_y


def is_eigen_positie(eigen_coordinaat: tuple,
                     opgegeven_coordinaat: tuple) -> bool:
    """
    Controleert of de opgegeven coordinaat niet zijn eigen coordinaat is.

    :param eigen_coordinaat: Eigen coordinaat als list.
    :param opgegeven_coordinaat: Opgegeven coordinaat als list.
    :return: True of False als het opgegeven coordinaat hetzelfde is.
    """
    return eigen_coordinaat == opgegeven_coordinaat


if __name__ == "__main__":
    main()
