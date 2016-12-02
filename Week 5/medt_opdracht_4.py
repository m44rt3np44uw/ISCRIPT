"""
Opdracht 4 - Bestanden kopieren

https://dodona.ugent.be/nl/exercises/1985652400/
"""


def kopieer(bronbestand: str, doelbestand: str) -> bool:
    """
    Kopieer de inhoud van een bronbestand naar het doelbestand.

    :param bronbestand: Naam van het bronbestand als string.
    :param doelbestand: Naam van het doelbestand als string.
    :return: Of het gelukt is.
    """
    # Probeer het kopieren.
    try:

        # Open het oude document.
        with open(bronbestand) as bron:

            # Haal de inhoud op.
            inhoud = bron.read()

            # Open het nieuwe document.
            with open(doelbestand, 'w') as doel:

                # Plaats de inhoud.
                print(inhoud, file=doel)

        # Het kopieren is gelukt
        return True

    # Het is niet gelukt.
    except:

        # Het kopieren is niet gelukt.
        return False


def main() -> None:
    """
    Opdracht 4 - Bestanden kopieren
    """
    # Bestand 1
    kopieer('medt_opdracht_4_bron.txt', 'medt_opdracht_4_doel.txt')


if __name__ == "__main__":
    main()
