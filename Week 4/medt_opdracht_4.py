"""
Opdracht 4 - Zoemzinnen

https://dodona.ugent.be/nl/exercises/1620493816/
"""
import random


def main() -> None:
    """
    Opdracht 4 - Zoemzinnen
    """
    # Buzz 1
    buzz1 = ('integrated', 'total', 'systematized', 'parallel', 'functional',
             'responsive', 'optional', 'synchronized', 'compatible',
             'balanced')

    # Buzz 2
    buzz2 = (
        'management', 'organizational', 'monitored', 'reciprocal', 'digital',
        'logistical', 'transitional', 'incremental', 'third-generation',
        'policy')

    # Buzz 3
    buzz3 = (
        'options', 'flexibility', 'capability', 'mobility', 'programming',
        'concept', 'time-phase', 'projection', 'hardware', 'contingency')

    # Zoemzin 1
    print(zoemzin1((buzz1, buzz2, buzz3)))

    # Zoemzin 2
    print(zoemzin2(buzz1, buzz2, buzz3))


def zoemzin1(buzzez: tuple) -> str:
    """
    Pakt een willekeurig woord uit elke woordenlijst, en voegt deze woorden
    samen tot één enkele string (in de volgorde van de gegeven woordenlijsten).

    :param buzzez: Een lijst met buzz lijsten als tuple.
    :return: een zoemzin als string.
    """
    # Zoemzin.
    zoemzin = []

    # Loop door elke lijst met buzz woorden heen.
    for buzz in buzzez:

        # Voeg een random woord toe uit de buzz lijst.
        zoemzin.append(random.choice(buzz))

    # Geef de zoemzin terug.
    return " ".join(zoemzin)


def zoemzin2(*args) -> str:
    """
    Pakt een willekeurig woord uit elke woordenlijst, en voegt deze woorden
    samen tot één enkele string (in de volgorde van de gegeven woordenlijsten).

    :param buzzez: Een lijst met buzz lijsten als tuple.
    :return: een zoemzin als string.
    """
    return zoemzin1(args)


if __name__ == "__main__":
    main()
