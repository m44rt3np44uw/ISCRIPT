"""
Opdracht 1 - Interessante getallen

https://dodona.ugent.be/nl/exercises/211647828/
"""


def main() -> None:
    """
    Opdracht 1 - Interessante getallen.
    """
    # Verkrjg het aantal testgevallen.
    aantal_testgevallen = verkrijg_aantal_testgevallen()

    # Verkrijg het opgegeven aantal testgevallen.
    testgevallen = verkrijg_testgevallen(aantal_testgevallen)

    # Ga door elk testgeval heen.
    for testgeval in testgevallen:
        # Geef het antwoord op elk testgeval.
        print(verkrijg_antwoord(int(testgeval)))


def verkrijg_antwoord(testgeval: int) -> int:
    """
    Geef antwoord op de vraag; vind het kleinste natuurlijk getal dat deelbaar
    is door nn en waarvan de som van de cijfers gelijk is aan nn.

    :param testgeval:
    :return:
    """
    # natuurlijk_getal
    natuurlijk_getal = 1

    # Een niet eindige loop.
    while True:

        # Totdat is_deelbaar en controleer_som beide waar zijn.
        if is_deelbaar(testgeval, natuurlijk_getal) and controleer_som(
                testgeval, natuurlijk_getal):
            break

        # Zo niet tel het getal op.
        natuurlijk_getal += 1

    # Geef het getal terug.
    return natuurlijk_getal


def is_deelbaar(testgeval: int, natuurlijk_getal: int) -> bool:
    """
    Controleer of het getal deelbaar is.

    :param testgeval: Het opgegeven testgeval als integer.
    :param natuurlijk_getal: Een natuurlijk getal als integer.
    :return: True of False op basis van de boven gestelde vraag.
    """
    return natuurlijk_getal % testgeval is 0


def controleer_som(testgeval: int, natuurlijk_getal: int) -> bool:
    """
    Contoleer of de losse digits van het natuurlijk getal gelijk zijn
    aan het opgegeven testgeval.

    :param testgeval: opgegeven testgeval als integer.
    :param natuurlijk_getal: opgegeven natuurlijk getal als integer.
    :return: True of False op basis van de bovengestelde vraag.
    """
    # De som van de digits/getallen lijst.
    som = sum(list(map(int, str(natuurlijk_getal))))

    # Geef terug of de getallen gelijk zijn aan elkaar.
    return testgeval is som


def verkrijg_aantal_testgevallen() -> int:
    """
    Verkrijg het aantal testgevallen.

    :return: Het aantal testgevallen als integer.
    """
    # Vraag
    vraag = "Aantal testgevallen"

    # Vraag het aantal testgevallen.
    aantal_testgevallen = stel_interger_vraag(vraag)

    # Controleer of het wel minder dan 50 testgevallen zijn.
    while 0 < aantal_testgevallen > 50:

        # Vraag het aantal testgevallen.
        aantal_testgevallen = stel_interger_vraag(vraag)

    # Geef het aantal testgevallen terug.
    return aantal_testgevallen


def verkrijg_testgevallen(aantal_testgevallen: int) -> list:
    """
    Verkrijg de gevraagde aantal testgevallen.

    :param aantal_testgevallen: Het gewenst aantal testgevallen.
    :return: lijst met testgevallen als list.
    """
    # Een lege lijst.
    testgevallen = []

    # Loop door elk testgeval heen.
    for testgeval in range(0, aantal_testgevallen):

        # Vraag
        vraag = "Testgeval " + str(testgeval + 1)

        # Vraag het testgeval.
        gegeven_testgeval = stel_interger_vraag(vraag)

        # Controleer of het testgeval wel tussen de 0 en de 101 ligt.
        while 0 < gegeven_testgeval > 100:

            # Zoniet stellen we de vraag opniew.
            gegeven_testgeval = stel_interger_vraag(vraag)

        # Voeg het gegeven testgeval toe.
        testgevallen.insert(testgeval, gegeven_testgeval)

    # Geef een lijst met testgevallen terug.
    return testgevallen


def stel_interger_vraag(vraag: str) -> int:
    """
    Verkrijg een antwoord als integer op een vraag.

    :param vraag: Vraag als string.
    :return: antwoord als integer.
    """
    return int(input(vraag + ": "))


if __name__ == "__main__":
    main()
