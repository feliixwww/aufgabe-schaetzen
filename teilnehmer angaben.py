teilnehmer = []

while True:
    eingabe = input("""Bitte gib deinen Namen ein und bestätige mit 'Enter', wenn alle Teilnehmer ihren Namen eingetragen haben, drücke nur 'Enter'
    > """)
    if eingabe == "":
        break
    teilnehmer.append(eingabe)

print("Die Namen der Teilnehmer sind:", teilnehmer)