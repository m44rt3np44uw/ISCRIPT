"""
Opdracht 5 - Luchthavens

https://dodona.ugent.be/nl/exercises/1748605282/
"""
from math import radians, sqrt, cos, sin, atan2, pow


def main() -> None:
    """
    Opdracht 5 - Luchthavens
    """
    # Lees de luchthavens
    luchthavens = lees_luchthavens('medt_opdracht_5_luchthavens.txt')

    # Luchthaven 1
    print(luchthavens['ADK'])

    # Luchthaven 2
    print(luchthavens['DCA'])

    # Luchthaven 3
    print(luchthavens['4OM'])

    # Afstand 1
    afstand_1 = afstand('P60', 'MSN', luchthavens)
    print("%.8f" % afstand_1)

    # Afstand 2
    afstand_2 = afstand('ADK', 'DCA', luchthavens)
    print("%.8f" % afstand_2)

    # Tussenlanding
    tussenlanding_1 = tussenlanding('ADK', 'DCA', luchthavens, 4000)
    print(tussenlanding_1)


def lees_luchthavens(bestandsnaam: str) -> dict:
    """
    Verkrijg alle luchthavens uit het opgegeven bestand.

    :param bestandsnaam: Bestandsnaam.
    :return: Een lijst met luchthavens als dictionary.
    """
    # Luchthavens
    luchthavens = dict()

    # Open het document.
    with open(bestandsnaam) as bestand:

        # Haal de inhoud op.
        inhoud = bestand.read()

        # Loop door elke rij heen.
        for rij_index, rij in enumerate(inhoud.split('\n')):

            # Split de kolommen op de tap.
            rij = rij.split('\t')

            # Controleer of het niet de header rij is.
            if rij_index is not 0:
                # Voeg het toe aan de dictionary.
                luchthavens.update({rij[0][1:-1]: (
                    float(rij[1]), float(rij[2]), rij[3], rij[4])})

    # Geef de lijst met luchthavens terug.
    return luchthavens


def afstand(luchthaven_code_1: str, luchthaven_code_2: str,
            luchthavens: dict) -> float:
    """

    :param luchthaven_code_1:
    :param luchthaven_code_2:
    :param luchthavens:
    :return:
    """
    # Luchthaven 1
    luchthaven_1 = luchthavens[luchthaven_code_1]

    # Luchthaven 2
    luchthaven_2 = luchthavens[luchthaven_code_2]

    # Haal de breedteligging en de lengteligging op.
    breedteligging_1, lengteligging_1 = luchthaven_1[0:2]
    breedteligging_2, lengteligging_2 = luchthaven_2[0:2]

    # Converteer naar radiaal.
    breedteligging_1 = radians(breedteligging_1)
    breedteligging_2 = radians(breedteligging_2)

    # Converteer naar radiaal.
    lengteligging_1 = radians(lengteligging_1)
    lengteligging_2 = radians(lengteligging_2)

    # Geef de afstand terug.
    return 6372.795 * atan2(sqrt(
        pow(cos(breedteligging_2) * sin(lengteligging_1 - lengteligging_2),
            2) + pow(cos(breedteligging_1) * sin(breedteligging_2) - sin(
                breedteligging_1) * cos(breedteligging_2) * cos(
                lengteligging_1 - lengteligging_2), 2)),
        sin(breedteligging_1) * sin(
            breedteligging_2) + cos(
            breedteligging_1) * cos(
            breedteligging_2) * cos(
            lengteligging_1 - lengteligging_2))


def tussenlanding(luchthaven_code_1: str, luchthaven_code_2: str,
                  luchthavens: dict, reikwijdte: int = 4000) -> str:
    """

    :param luchthaven_code_1:
    :param luchthaven_code_2:
    :param luchthavens:
    :param reikwijdte:
    :return:
    """
    # Verkrijg de afstand tussen de 2 luchthavens.
    de_afstand = afstand(luchthaven_code_1, luchthaven_code_2, luchthavens)

    # Kleinste afstand
    kleinste_afstand = de_afstand * 10000

    # Luchthaven code.
    luchthaven_code = ""

    # Loop door alle luchthavens heen.
    for luchthaven in luchthavens:

        # Controleer of de luchthaven niet het begin op het eindpunt is.
        if luchthaven not in [luchthaven_code_1, luchthaven_code_2]:

            # Verkrijg de afstand van punt A naar C.
            afstand_a_naar_c = afstand(luchthaven_code_1, luchthaven,
                                       luchthavens)

            # Verkrijg de afstand van punt C naar B.
            afstand_c_naar_b = afstand(luchthaven, luchthaven_code_2,
                                       luchthavens)

            # Totale afstand van punt A naar B.
            afstand_a_naar_b = afstand_a_naar_c + afstand_c_naar_b

            # Controleer of beide punten we te bereiken zijn.
            if afstand_a_naar_c <= reikwijdte and \
                    afstand_c_naar_b <= reikwijdte:

                # Contoleer of van punt A naar B korter is.
                if afstand_a_naar_b < kleinste_afstand:

                    # Sla de afstand op.
                    kleinste_afstand = afstand_a_naar_b

                    # Sla de luchthaven code op.
                    luchthaven_code = luchthaven

    # Controleer of er een luchthaven gevonden is en de
    # afstand niet binnen bereik valt.
    if luchthaven_code is "" or de_afstand < reikwijdte:
        return None

    # Is dat niet het geval.
    else:

        # Geef de luchthaven code terug.
        return luchthaven_code


if __name__ == "__main__":
    main()
