teilnehmer = []

while True:
    eingabe = input("""Bitte gib deinen Namen ein und bestätige mit 'Enter', wenn alle Teilnehmer ihren Namen eingetragen haben, drücke nur 'Enter'
    > """)
    if eingabe == "":
        break
    teilnehmer.append(eingabe)

print("Die Namen der Teilnehmer sind:", teilnehmer)

fibunacci_folge = [0, 1, 1]
i = 100

while i > 0:
    zahl = fibunacci_folge[-1] + fibunacci_folge[-2]
    fibunacci_folge.append(zahl)
    i = i - 1

lange = len(teilnehmer)
a = 0
schätzungenliste = []

while lange > 0:
    schätzung = int(input(f"Hallo {teilnehmer[a]}, gibt bitte deine Schätzung als Ganzzahl aus der Fibonacci-Folge ein und bestätige mit <Enter>."))

    if schätzung in fibunacci_folge:
        schätzungenliste.append(schätzung)
        lange - 1
        a = a + 1
        if a == lange:
            break