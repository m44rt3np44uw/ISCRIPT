"""
Opdracht 1 - Tijdmeting op Mars

https://dodona.ugent.be/nl/exercises/1813154454/
"""


def main():
    """
    Opdracht 1 - Tijdmeting op Mars

    :return: void
    """

    # Sol als aarde tijd.
    sol = "24:39:35.244"

    # Sol opgesplitst in uren, minuten en seconden.
    (sol_uren, sol_minuten, sol_seconden) = sol.split(":")

    # Sol omgerekent naar seconden.
    sol_in_seconden = (int(sol_uren) * 60 * 60) + (int(sol_minuten) * 60) + (
        float(sol_seconden))

    # Het aantal sol dagen wordt opgeslagen.
    sol_dagen = int(input("vul het aantal sol dagen in: "))

    # Het aantal sol dagen in seconden.
    sol_dagen_in_seconden = int(sol_dagen) * float(sol_in_seconden)

    # http://stackoverflow.com/a/3895091/2940668
    # aarde dagen en overige seconden
    (aarde_dagen, overige_seconden) = converteer_tijd(sol_dagen_in_seconden,
                                                      int(1 * 60 * 60 * 24))

    # aarden uren en overige seconden
    (aarde_uren, overige_seconden) = converteer_tijd(overige_seconden,
                                                     int(1 * 60 * 60))

    # aarde minuten en overige seconden
    (aarde_minuten, overige_seconden) = converteer_tijd(overige_seconden,
                                                        int(1 * 60))

    # aarde secondenen overige seconden
    (aarde_seconden, aarde_miliseconden) = str(overige_seconden).split(".")

    # print de string.
    print(sol_dagen, "sol =", int(aarde_dagen),
          markup(aarde_dagen, "dagen", "dag"),
          int(aarde_uren),
          markup(aarde_uren, "uren", "uur"),
          int(aarde_minuten),
          markup(aarde_minuten, "minuten", "minuut"),
          "en",
          int(aarde_seconden),
          markup(int(aarde_seconden), "seconden", "seconde"))


def converteer_tijd(tijd: float, formule_naar_seconden: int) -> (
        float, float):
    """
    Converteert een float naar een tijdsnotatie als int en
    het overige als float.

    :param tijd:                    als float
    :param formule_naar_seconden:   als int
    :return:                        (tijd: float, overige_seconden: float)
    """
    return divmod(tijd, formule_naar_seconden)


def markup(getal, string_een, string_twee) -> str:
    """
    Maak een mooie markup.

    :param getal:       int als dagen, uren, minuten of seconden.
    :param string_een:  string als 'dagen', 'uren', 'minuten' of 'seconden'.
    :param string_twee: string als 'dag', 'uur', 'minuut' of 'seconde'.
    :return:            string string_een of string_twee
    """
    if getal > 1:
        return string_een
    else:
        return string_twee


if __name__ == "__main__":
    main()
