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


def schätzen():
    lange = len(teilnehmer)
    a = 0
    global schätzungenliste
    schätzungenliste = []


    while lange > 0:
        while True:
            try:
                schätzung = int(input(f"""Hallo {teilnehmer[a]}, gib bitte deine Schätzung als Ganzzahl aus der Fibunacci-Folge ein und bestätige mit 'Enter'
> """))
                break
            except ValueError:
                print("Fehler: Bitte geben Sie eine Zahl ein.")

        if schätzung in fibunacci_folge:
            schätzungenliste.append(schätzung)
            lange - 1
            a = a + 1
            if a == lange:
                break
        else:
            print("Die zahl ist nicht in der Fibunacci-Folge!")

schätzen()

TN_1 = schätzungenliste[0]
Anzahl_Teilnehmer = (len(schätzungenliste))
i = 0
a = 1
while Anzahl_Teilnehmer > i:
    if TN_1 != schätzungenliste[a]:
        print(F"""Eure Schätzwerte sind: {schätzungenliste}
Diskutiert die Komplexität und möglichen Risiken der Umsetzung und gebt eure Schätzung erneut ein!""")
        schätzen()
        break
    a += 1
    if a == Anzahl_Teilnehmer:
        break
    i += 1
def E_Schätzen():
    Erneut_Schätzen = input(F"""Ihr habt das Feature mit {TN_1} Storypoints bewertet!
Wollt ihr ein weiteres Feature schätzen? (y/n)""")
    if Erneut_Schätzen == "n":
        quit()
    elif Erneut_Schätzen == "y":
        schätzen()
    else:
        E_Schätzen()
E_Schätzen()