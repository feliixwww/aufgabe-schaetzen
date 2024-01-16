def meine_funktion(*teilnehmer):
    for i, teilnehmer_name in enumerate(teilnehmer):
        variable_name = f"teilnehmer_{i}"
        exec(f"{variable_name} = '{teilnehmer_name}'")
        print(f"Variable {variable_name} wurde erstellt und hat den Wert {teilnehmer_name}")

meine_funktion(4)