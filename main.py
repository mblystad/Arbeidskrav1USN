# ------------------------------------------------------------------------------------------------------------
# Oppgave
#
# Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved
# elbil sammenliknet med bensinbil.
#
# Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for
# bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se
# bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil
# og bensinbil).
#
# Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)
#
# Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
# Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
# Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
# Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
# Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
# ------------------------------------------------------------------------------------------------------------


# Velkomst melding, introduserer bruker for programmets funksjon med FEET ASCII LOGO
print(r"""
___________.____      ____   _____________  _____________________ _______    _________.___ _______   
\_   _____/|    |     \   \ /   /   _____/  \______   \_   _____/ \      \  /   _____/|   |\      \  
 |    __)_ |    |      \   Y   /\_____  \    |    |  _/|    __)_  /   |   \ \_____  \ |   |/   |   \ 
 |        \|    |___    \     / /        \   |    |   \|        \/    |    \/        \|   /    |    \
/_______  /|_______ \    \___/ /_______  /   |______  /_______  /\____|__  /_______  /|___\____|__  /
        \/         \/                  \/           \/        \/         \/        \/             \/
                """)
print("Velkommen til kalkulatoren for bensin og elbil")

# Spør bruker om hvor langt vedkommende skal kjøre, med "while" løkke for å sjekke at bruker skriver tall.

km = 0
while True:
  try:
     km = int(input("Hvor langt skal du kjøre i år (KM)?"))
  except ValueError:
     print("Du må skrive tall, ikke bokstaver, prøv igjen.")
     continue
  else:
     break


# Beregning av utgifter utifra oppgave teksten, med omgjøring fra float til int for mer brukervennlig output. Bruker input (km) gjøres også om til int.
elbom = int(0.1*int(km))
bensinbom = int(0.3*int(km))
el_drivstoff = int((0.2*int(km))*2)
bensin_drivstoff = int(1*int(km))
aarsavgift = int(8.38*365)

# Flag for å sjekke om bruker velger bensin eller ikke. Inngår i senere funksjon for å vise detaljerte utgifter.
bensin = False

# Bruker bes oppgi om vedkommende kjører bensinbil eller ikke. Om ikke antas El, siden dette er satt av oppgavens
# rammer, og det står i første instruksjoner gitt brukeren.
biltype =input("Har du bensinbil? Ja/Nei")

# Liste med gyldige input som brukes for å sjekke om input er ja eller nei.
liste_for_aksepterte_valg = ["ja", "nei"]

# While løkke som sjekker mot listen over, og gir bruker ny prompt om brukerinput ikke er ja eller nei.
while biltype.lower() not in liste_for_aksepterte_valg:
    print("Du må skrive ja eller nei")
    biltype = input("Har du bensinbil? Ja/Nei (Om ikke antas EL-bil)")

# Hvis løkke som sjekker om bruker har bensinbil. Setter bensin til true. Plusser sammen utgifter i el (el_aarspris) og bensin (aarspris).
# Skriver hva det vil koste i konsollen, og forskjellen mellom bensin og el.
if biltype.lower() == "ja":
    bensin = True
    aarspris = 7500 + bensin_drivstoff + bensinbom + aarsavgift
    el_aarspris = 5000 + aarsavgift + el_drivstoff + elbom
    print(f"Du kjører bensinbil og skal betale {aarspris}kr årlige kostnader.  \nElbil vil koste {el_aarspris}kr, og forskjellen i årlig utgift blir da {aarspris-el_aarspris}kr.)")
else:
    el_aarspris = 5000 + aarsavgift + el_drivstoff +elbom
    aarspris = 7500 + bensin_drivstoff + bensinbom + aarsavgift
    print(f"Du kjører elbil og skal betale {el_aarspris}kr i årlige kostnader. \nBensinbil vil koste {aarspris}kr, og forskjellen i årlig utgift blir da {aarspris-el_aarspris}kr.")

# Spør bruker om det ønskes detaljert oversikt over utgiftene.
oversikt = input("Vil du ha en oversikt over detaljerte utgifter for din biltype? Ja/Nei")

# Sjekker at bruker skriver ja/nei mot listen liste_for_aksepterte_valg.
while oversikt.lower() not in liste_for_aksepterte_valg:
    print("Du må skrive ja eller nei")
    oversikt = input("Vil du ha en oversikt over detaljerte utgifter for din biltype? Ja/Nei")

# Hvis løkke som sjekker om det var valgt bensin (flag: bensin = true/false). Hvis bensin = True skrives utgiftene for bensinbil.
# Hvis bensin=False, skrives utgiftene for elbil.
# Uansett skrives en avslutningsmelding (både for bensin, elbil, men også dersom det ikke ønskes noen detaljerte utgifter).
if oversikt.lower() == "ja" and bensin:
        print(f"Du betaler {bensinbom}kr for bompasseringer, {aarsavgift}kr i trafikkforsikringsavgift, \nog {bensin_drivstoff}kr for bensin.")
        print("Lykke til med bilkjøp!")
elif oversikt.lower() == "ja" and not bensin :
        print(
                f"Du betaler {elbom}kr for bompasseringer, {aarsavgift}kr i trafikkforsikringsavgift, \nog {el_drivstoff}kr for lading.")
        print("Lykke til med bilkjøp!")
else:
    print("Lykke til med bilkjøp!")
    pass
