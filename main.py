teilnehmer = []


def teilnehmerabfrage():
    while True:
        eingabe = input("""Bitte gib deinen Namen ein und bestätige mit 'Enter', wenn alle Teilnehmer ihren Namen
eingetragen haben, drücke nur 'Enter'
    > """)
        if eingabe == "":
            if len(teilnehmer) < 2:
                teilnehmerabfrage()
            break
        teilnehmer.append(eingabe)


teilnehmerabfrage()


print(f"""
Die Namen der Teilnehmer sind:, {teilnehmer}""")

fibunacci_folge = [0, 1, 1]
fibunacci_wiederholungen = 100

while fibunacci_wiederholungen > 0:
    zahl = fibunacci_folge[-1] + fibunacci_folge[-2]
    fibunacci_folge.append(zahl)
    fibunacci_wiederholungen = fibunacci_wiederholungen - 1


def schaetzen():
    lange = len(teilnehmer)
    teilnehmer_position_in_der_liste = 0
    global schaetzungenliste
    schaetzungenliste = []

    while lange > 0:
        while True:
            try:
                schaetzung = int(input(f"""
Hallo {teilnehmer[teilnehmer_position_in_der_liste]}, gib bitte deine Schätzung als Ganzzahl aus der
Fibunacci-Folge ein und bestätige mit 'Enter'
> """))
                break
            except ValueError:
                print("Fehler: Bitte geben Sie eine Zahl ein.")

        if schaetzung in fibunacci_folge:
            schaetzungenliste.append(schaetzung)
            lange - 1
            teilnehmer_position_in_der_liste = teilnehmer_position_in_der_liste + 1
            if teilnehmer_position_in_der_liste == lange:
                break
        else:
            print("Die zahl ist nicht in der Fibunacci-Folge!")

    global TN_1
    TN_1 = schaetzungenliste[0]
    anzahl_teilnehmer = (len(schaetzungenliste))
    wiederholung_vergleich = 0
    schaetzungsindex = 1
    while anzahl_teilnehmer > wiederholung_vergleich:
        if TN_1 != schaetzungenliste[schaetzungsindex]:
            print(f"""Eure Schätzwerte sind: {schaetzungenliste}
Diskutiert die Komplexität und möglichen Risiken der Umsetzung und gebt eure Schätzung erneut ein!
""")
            schaetzen()
        schaetzungsindex += 1
        if schaetzungsindex == anzahl_teilnehmer:
            break
        wiederholung_vergleich += 1
    erneut_def_schaetzen()


def erneut_def_schaetzen():
    erneut_schaetzen = input(f"""
Ihr habt das Feature mit {TN_1} Storypoints bewertet!
Wollt ihr ein weiteres Feature schätzen? (y/n)
> """)
    if erneut_schaetzen == "n":
        quit()
    elif erneut_schaetzen == "y":
        schaetzen()
    else:
        erneut_def_schaetzen()


schaetzen()

