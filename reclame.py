from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, oude_prijs, korting):
    nieuwe_prijs = oude_prijs * (1 - korting)
    nieuwe_prijs = f"{nieuwe_prijs:.2f}"
    reclame_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {oude_prijs} euro voor {nieuwe_prijs} euro."
    return reclame_tekst

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = (totaal*btw)
    Inkomsten_totaal_tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"
    return Inkomsten_totaal_tekst

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    hoogste_waarde = max(mijn_lijst)
    Laagste_waarde = min(mijn_lijst)
    return hoogste_waarde, Laagste_waarde

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    inkomsten_per_dag = sum(mijn_lijst) / len(mijn_lijst)
    inkomsten_per_dag_tekst = f"De gemiddelde inkomsten deze week zijn {inkomsten_per_dag} euro"
    return inkomsten_per_dag_tekst

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    meervoudig_invoer = laag_en_hoog(invoer_lijst)
    return meervoudig_invoer

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie([10, 5, 3, 2, 1, 2, 9]))
