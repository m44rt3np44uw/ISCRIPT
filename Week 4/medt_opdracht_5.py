"""
Opdracht 5 - Zomertijd

https://dodona.ugent.be/nl/exercises/116986379/
"""
from datetime import date, timedelta, datetime


def zomertijd(jaartal: int) -> date:
    """
    Krijg datum die voorstelt waarop in de Europese Unie de zomertijd ingaat
    (laatste zondag van maart) in het opgegeven jaar.

    :param jaartal: Een jaartal als integer.
    :return: De datum wanneer de zomertijd ingaat als date.
    """
    # Laatste dag in maart.
    laatste_dag_in_maart = date(jaartal, 4, 1) - timedelta(days=1)

    # Geef de laatste zondag van de maand terug.
    return verkrijg_laatste_zondag(laatste_dag_in_maart)


def wintertijd(jaartal: int) -> date:
    """
    Krijg datum die voorstelt waarop in de Europese Unie de wintertijd ingaat
    (laatste zondag van oktober) in het opgegeven jaar.

    :param jaartal: Een jaartal als integer.
    :return: De datum wanneer de wintertijd ingaat als date.
    """
    # Laatste dag in oktober.
    laatste_dag_in_oktober = date(jaartal, 11, 1) - timedelta(days=1)

    # Geef de laatste zondag van de maand terug.
    return verkrijg_laatste_zondag(laatste_dag_in_oktober)


def verkrijg_laatste_zondag(laatste_dag_in_de_maand: date) -> date:
    """
    Verkrijg de laatste zondag van de opgegeven maand.

    :param laatste_dag_in_de_maand: Laatste dag in de maand als date.
    :return: Laatste zondag van de maand als date.
    """
    # Wintetijd datum
    laatste_zondag = laatste_dag_in_de_maand

    # Ga door zolang de dag niet gelijk is aan zondag.
    while laatste_zondag.weekday() is not 6:
        # Haal er 1 dag vanaf.
        laatste_zondag -= timedelta(1)

    # Geef de laatste zondag van de maand terug.
    return laatste_zondag


def klok(datum: str) -> str:
    """
    De functie geeft als resultaat een string die aangeeft of de klok op
    de opgegeven datum in zomertijd of wintertijd staat.

    :param datum: Datum als string DD/MM/YYYY
    :return: zomertijd of wintertijd als string.
    """
    # Converteer de string datum naar een date object.
    datum = datetime.strptime(datum, "%d/%m/%Y").date()

    # Wintertijd
    datum_zomertijd = zomertijd(datum.year)
    datum_wintertijd = wintertijd(datum.year)

    # Controleer of de zomertijd ingaat.
    if datum == datum_zomertijd:
        return "omschakeling van wintertijd naar zomertijd"

    # Controleer of de wintertijd ingaat.
    elif datum == datum_wintertijd:
        return "omschakeling van zomertijd naar wintertijd"

    # Controleer of de zomertijd is ingegaan.
    elif datum_wintertijd < datum > datum_zomertijd:
        return "wintertijd"

    # Controleer of de wintertijd is ingegaan.
    elif datum_wintertijd > datum > datum_zomertijd:
        return "zomertijd"


def main() -> None:
    """
    Opdracht 5 - Zomertijd
    """
    # Zomertijd 2013
    print(zomertijd(2013))

    # Zomertijd 2014
    print(zomertijd(2014))

    # Zomertijd 2015
    print(zomertijd(2015))

    # Lege regel.
    print("")

    # Wintertijd 2013
    print(wintertijd(2013))

    # Wintertijd 2014
    print(wintertijd(2014))

    # Wintertijd 2015
    print(wintertijd(2015))

    # Lege regel.
    print("")

    # Klok 1
    print(klok('27/06/2013'))

    # Klok 2
    print(klok('27/11/2013'))

    # Klok 3
    print(klok('31/03/2013'))

    # Klok 4
    print(klok('27/10/2013'))


if __name__ == "__main__":
    main()
