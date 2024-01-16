Schätzungsliste = []
TN_1 = Schätzungsliste[0]
Anzahl_Teilnehmer = (len(Schätzungsliste)
i = 0
a = 1
while Anzahl_Teilnehmer > i:
    if TN_1 != Schätzungsliste[a]
        print(F"""Eure Schätzwerte sind: {Schätzungsliste}
Diskutiert die Kemploxität und möglichen Risiken der Umsetzung und gebt eure Schätzung erneut ein!""")
        schätzen()
        break
    a += 1
    i += 1
def E_Schätzen:
    Erneut_Schätzen = input(F"""Ihr habt das Feature mit {TN_1} Storypoints  bewertet 
    Wollt ihr ein weiteres Feature schätzen? (y/n)""")
    if Erneut_Schätzen = "n":
        quit()
    elif Erneut_Schätzen = "y":
        schätzen()
    else:
        E_Schätzen()
E_Schätzen()
