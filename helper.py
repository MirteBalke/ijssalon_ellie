def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
    uit = [] # lege lijst maken
    uit.append(tekst) # voeg de tekst toe als eerste element
    uit.append("=" * len(tekst)) # voeg een string toe met =-tekens, gelijk aan de lengte van de tekst
    return uit

def som(data):
    totaal_values = sum(data.values())
    return totaal_values
