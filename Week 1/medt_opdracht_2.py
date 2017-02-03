"""
Opdracht 2 - Radialen naar graden

https://dodona.ugent.be/nl/exercises/975017137/
"""
from math import pi


def tijd_berekening(tijd: float) -> (float, float):
    """
    Converteert een float naar een tijdsnotatie als int en
    het overige als float.

    :param tijd: tijd als float.
    :return: (float, float)
    """
    return divmod(tijd * 60, 1)


def radiaal_naar_getal(aantal_radialen: float) -> float:
    """
    Coverteer een radiaal naar een komma getal.

    :param aantal_radialen: radiaal als float.
    :return:                radiaal geconverteerd naar een float.
    """
    return (180 / pi) * aantal_radialen


def main() -> None:
    """
    Opdracht 2 - Radialen naar graden

    Formule
    1 radiaal = 180 / 3.1415 = 57.297
    """

    # invoer in radialen.
    invoer_radialen = float(input("Voer het aantal radialen in: "))

    # radialen als getal
    radiaal_als_getal = radiaal_naar_getal(invoer_radialen)

    # Grootte van de hoek in graden
    grootte_van_de_hoek_in_graden = int(radiaal_als_getal)

    # Uren als een komma getal.
    uren = float(float(radiaal_als_getal) - int(radiaal_als_getal))

    # Uren en minuten.
    (minuten, overige_seconden) = tijd_berekening(uren)

    # Minuten en seconden.
    (seconden, overige_seconden) = tijd_berekening(overige_seconden)

    # Print het antwoord in de console.
    print(int(grootte_van_de_hoek_in_graden), "\n", int(minuten), "\n",
          int(seconden))


if __name__ == "__main__":
    main()
