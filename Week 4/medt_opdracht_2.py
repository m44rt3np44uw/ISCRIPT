"""
Opdracht 2 - 3 + 1 gratis

https://dodona.ugent.be/nl/exercises/751779411/
"""


def samen(prijzen: list) -> float:
    """
    Samen is een methode die het totaalbedrag teruggeeft dat je zal
    moeten betalen als je slechts één keer langs de kassa passeert
    om de gegeven reeks producten samen aan te kopen.

    :param prijzen: Een lijs met prijzen als list.
    :return: De totaalkosten als float.
    """
    # Aantal producten gratis.
    aantal_producten_gratis = round(len(prijzen) / 4)

    # Aantal te betalen producten.
    aantal_te_betalen_producten = len(prijzen) - aantal_producten_gratis

    # Sorteer de prijzen
    gesorteerde_prijzen = verkrijg_gesorteerde_prijzen(prijzen)

    # Geef het totaal bedrag terug.
    return sum(gesorteerde_prijzen[0:aantal_te_betalen_producten])


def groeperen(prijzen: list) -> list:
    """
    Geeft een lijst van tuples terug, waarbij elk tuple minimaal 1 en
    maximaal 4 floating point getallen bevat die gesorteerd
    zijn van groot naar klein.

    :param prijzen: Een lijst met prijzen als list.
    :return: Een gersorteerde lijst met prijzen in groepjes van 4.
    """
    # Sorteer de prijzen
    gesorteerde_prijzen = verkrijg_gesorteerde_prijzen(prijzen)

    # Een lijst met gegroepeerde producten.
    groep = []

    # Ga door de hele lijst heen in stappen van 4.
    for x in range(0, len(gesorteerde_prijzen), 4):
        # Voeg het groepje producten toe aan de groep.
        groep.append(tuple(gesorteerde_prijzen[x:x + 4]))

    # Geef de subgroepen terug.
    return groep


def gegroepeerd(prijzen: list) -> float:
    """
    Deze methode geeft het totaalbedrag terug dat je zal moeten betalen als
    je meerdere keren langs de kassa passeert om de gegeven reeks producten
    in groepjes van maximaal vier producten aan te kopen.

    :param prijzen: Een lijst met producten.
    :return: De kosten van de producten via bovenstaande manier.
    """
    # Verkrijg de pijzen gegroepeerd.
    prijzen_gegroepeerd = groeperen(prijzen)

    # Totale kosten.
    totale_kosten = 0

    # Ga door elke groep producten heen.
    for groep in prijzen_gegroepeerd:

        # Controleer of het een groep van 4 producten is.
        if len(groep) is 4:

            # Dat betalen we alleen voor de eerste 3 producten.
            totale_kosten += sum(groep[:3])

        # Zo niet?
        else:

            # Dan betalen we voor alle producten.
            totale_kosten += sum(groep)

    # Geef de totale kosten terug.
    return totale_kosten


def winst(prijzen: list) -> float:
    """
    Geef de winst terug die je maakt als je de strategie gebruikt waarbij
    je meerdere keren langs de kassa passeert, ten opzichte van de prijs
    die je zou betalen als je slechts één keer langs de kassa zou passeren.

    :param prijzen: Een lijst met prijzen als list.
    :return: De winst die je zou maken als float.
    """
    # De prijs samen.
    prijs_samen = samen(prijzen)

    # De prijs gegroepeerd.
    prijs_gegroepeerd = gegroepeerd(prijzen)

    # Geef de winst terug.
    return prijs_samen - prijs_gegroepeerd


def verkrijg_gesorteerde_prijzen(prijzen: list) -> list:
    """
    Sorteer de prijzen van hoog naar laag.

    :param prijzen: Een lijst met prijzen op verschillende volgorde als list.
    :return: Een gesorteerde lijst prijzen als list.
    """
    return sorted(prijzen, reverse=True)


def main() -> None:
    """
    Opdracht 2 - 3 + 1 gratis
    """
    # Alle prijzen van bepaalde producten in een lijst.
    prijzen = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]

    # Prijzen via de methode samen
    prijs_samen = samen(prijzen)

    # Prijzen via de methode groeperen.
    prijzen_gegroepeerd = groeperen(prijzen)

    # Prijs via de methode gegroepeerd.
    prijs_gegroepeerd = gegroepeerd(prijzen)

    # De winst
    de_winst = winst(prijzen)

    # Print samen
    print("%.2f" % prijs_samen)

    # Print groeperen
    print(prijzen_gegroepeerd)

    # Print gegroepeerd
    print("%.2f" % prijs_gegroepeerd)

    # Print de winst.
    print("%.2f" % de_winst)


if __name__ == "__main__":
    main()
