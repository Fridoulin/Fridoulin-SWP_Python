import firma as f

Person = []
Mitarbeiter = []
Gruppenleiter = []

def add_Person():
    return (f.Person(f.Sex.Mann, "Jochen", "Scherzer", f.Abteilung.einkauf),
    f.Person(f.Sex.Mann, "Konstantin", "Bauschinger", f.Abteilung.einkauf),
    f.Person(f.Sex.Frau, "Maria", "Rosenblum", f.Abteilung.produktion),
    f.Person(f.Sex.Frau, "Helge", "Werkner", f.Abteilung.verkauf),
    f.Person(f.Sex.Mann, "Reiner", "Adelman", f.Abteilung.produktion),
    f.Person(f.Sex.Mann, "Justin", "Bodenheimer", f.Abteilung.verkauf),
    f.Person(f.Sex.Mann, "Phillip", "Strassmann", f.Abteilung.produktion),
    f.Person(f.Sex.Mann, "Antonin", "Tendler", f.Abteilung.einkauf))

def add_Mitarbeiter():
    return (f.Mitarbeiter(f.Sex.Mann, "Sebastian", "Rimml", f.Abteilung.einkauf, 7541),
    f.Mitarbeiter(f.Sex.Mann, "Manuel", "Repetschnig", f.Abteilung.produktion, 7695),
    f.Mitarbeiter(f.Sex.Mann, "David", "Seidl", f.Abteilung.produktion, 7864),
    f.Mitarbeiter(f.Sex.Frau, "Helga", "Santler", f.Abteilung.verkauf, 1452),
    f.Mitarbeiter(f.Sex.Frau, "Sofia", "Santner", f.Abteilung.einkauf, 4566),
    f.Mitarbeiter(f.Sex.Mann, "David", "Simma", f.Abteilung.einkauf, 5978),
    f.Mitarbeiter(f.Sex.Frau, "Daniel", "Niederhauser", f.Abteilung.einkauf, 7878))

def add_Gruppenleiter():
    return (f.Gruppenleiter(f.Sex.Mann,"Torben", "Ullmer", f.Abteilung.einkauf, 9512, 1),
    f.Gruppenleiter(f.Sex.Mann, "Kaleb", "Halberstam", f.Abteilung.produktion, 9365, 2),
    f.Gruppenleiter(f.Sex.Frau, "Tina", "Strauss", f.Abteilung.verkauf, 9874, 3))

def get_Abteilung():
    return len(f.Abteilung)

def get_Anzahl():
    return len(Mitarbeiter), len(Gruppenleiter)

def get_MannZuFrauAnteil():
    mann = 0
    for p in Person:
        if p.Sex == f.Sex.Mann:
            mann += 1
    for m in Mitarbeiter:
        if m.Sex == f.Sex.Mann:
            mann += 1
    for g in Gruppenleiter:
        if g.Sex == f.Sex.Mann:
            mann += 1
    print("X", mann)
    return "%: " + str(round(mann / (len(Person) + len(Mitarbeiter) + len(Gruppenleiter)), 2) * 100) + " / " + str(round(
        (len(Person) + len(Mitarbeiter) + len(Gruppenleiter) - mann) / (
                len(Person) + len(Mitarbeiter) + len(Gruppenleiter)), 2) * 100)

def get_Meisten_Mitarbeiter(ab):
    anzahl_Mitarbeiter = 0
    for p in Person:
        if p.Abteilung == ab:
            anzahl_Mitarbeiter += 1

    for m in Mitarbeiter:
        if m.Abteilung == ab:
            anzahl_Mitarbeiter += 1

    for g in Gruppenleiter:
        if g.Abteilung == ab:
            anzahl_Mitarbeiter += 1

    return anzahl_Mitarbeiter

if __name__ == '__main__':
    Person = add_Person()
    Mitarbeiter = add_Mitarbeiter()
    Gruppenleiter = add_Gruppenleiter()
    print("Mitarbeiter: " + str(get_Anzahl()[0]))
    print("Gruppenleiter: " + str(get_Anzahl()[1]))
    print("Anzahl Abteilungen: " + str(get_Abteilung()))
    print("Gesamtanzahl Mitarbeiter: ")
    for d in f.Abteilung:
        print(str(d._name_) + " " + str(get_Meisten_Mitarbeiter(d)))
    print(get_MannZuFrauAnteil())
