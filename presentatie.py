def presenteer(data, totaal):
    for sleutel, waarde in data.items():
        print(f"{sleutel} : {waarde} euro")
    print("=" * 26)
    print(f"totaal : {totaal} euro")
    
