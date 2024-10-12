# Veiledere: Studentassistentene.
#
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

# Velkomst melding, introduserer bruker for programmets funksjon.
print("Velkommen til kalkulatoren for bensin og elbil")

# Spør bruker om hvor langt vedkommende skal kjøre.
km = int(input("Hvor langt skal du kjøre i km i år?"))

# Beregning av utgifter utifra oppgave teksten, med omgjøring fra float til int for mer brukervennlig output.
elbom = int(0.1*km)
bensinbom = int(0.3*km)
el_drivstoff = int((0.2*km)*2)
bensin_drivstoff = int(1*km)
aarsavgift = int(8.38*365)

# Flag for å sjekke om bruker velger bensin eller ikke. Inngår i senere funksjon for å vise detaljerte utgifter.
bensin = False

# Bruker best oppgi om vedkommende kjører bensinbil eller ikke. Om ikke antas El, siden dette er satt av oppgavens rammer.
biltype =input("Har du bensinbil? Ja/Nei")
# Hvis løkke som sjekker om svaret er ja eller nei (i.e. om bruker input med småbokstaver er "ja").
if biltype.lower() == "ja":
    bensin = True
    aarspris = 7500 + bensin_drivstoff + bensinbom + aarsavgift
    el_aarspris = 5000 + aarsavgift + el_drivstoff + elbom
    print(f"Du kjører bensinbil og skal betale {aarspris}kr årlige kostnader.  \nElbil vil koste {el_aarspris}kr, og forskjellen i årlig utgift blir da {aarspris-el_aarspris}kr.)")
else:
    el_aarspris = 5000 + aarsavgift + el_drivstoff +elbom
    aarspris = 7500 + bensin_drivstoff + bensinbom + aarsavgift
    print(f"Du kjører elbil og skal betale {el_aarspris}kr i årlige kostnader. \nBensinbil vil koste {aarspris}kr, og forskjellen i årlig utgift blir da {aarspris-el_aarspris}kr.")
oversikt = input("Vil du ha en oversikt over detaljerte utgifter for din biltype? Ja/Nei")

if oversikt.lower() == "ja":
    if bensin:
        print(f"Du betaler {bensinbom}kr for bompasseringer, {aarsavgift}kr i trafikkforsikringsavgift, \nog {bensin_drivstoff}kr for bensin.")
        print("Lykke til med bilkjøp!")
    else:
        print(
            f"Du betaler {elbom}kr for bompasseringer, {aarsavgift}kr i trafikkforsikringsavgift, \nog {el_drivstoff}kr for lading.")
        print("Lykke til med bilkjøp!")
else:
    print("Lykke til med bilkjøp!")

