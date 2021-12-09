import firma as f


class Company:

    def __init__(self):
        self.persons = []
        self.department_counters = {}
        [self.department_counters.setdefault(i, 0) for i in f.Abteilung]

    def add_person(self, p: f.Person):
        if not isinstance(p, f.Person):
            raise Exception()
        self.persons.append(p)
        self.department_counters[p.Abteilung] += 1

    def add_persons(self, l: list):
        for p in l:
            self.add_person(p)

    def allePersonen(self):
        return self.persons

    def alleMitarbeiter(self):
        ms = []
        for m in self.persons:
            if isinstance(m, f.Mitarbeiter):
                ms.append(m)
        return ms

    def alleGruppenleiter(self):
        gs = []
        for g in self.persons:
            if isinstance(g, f.Gruppenleiter):
                gs.append(g)
        return gs

    def getAbteilungen(self):
        return f.Abteilung

    def meistenArbeiter(self):
        return max(self.department_counters, key=self.department_counters.get)

    def getGender(self, s: f.Sex):
        if not isinstance(s, f.Sex):
            raise Exception()
        gs = []
        for g in self.persons:
            if g.Sex == s:
                gs.append(g)
        return gs

    def prozentMaennerzuFrauen(self, s: f.Sex):
        return 100 * len(self.getGender(s)) / len(self.persons)

    def getArbeiterNachAbteilungen(self, abteilung: f.Abteilung):
        if not isinstance(abteilung, f.Abteilung):
            raise Exception()
        es = []
        for e in self.persons:
            if e.abteilung == abteilung:
                es.append(e)
        return es

def ausgabe():
    print(f'Alle Personen: ',len(c.allePersonen()) ,f' \nAlle Mitarbeiter:',len(c.alleMitarbeiter()),'\nAlle Gruppenleiter',len(c.alleGruppenleiter()))
    print(f'Alle Abteilungen: ',len(c.getAbteilungen()))
    print(f'Abteilung mit den meisten Mitarbeitern: ',c.meistenArbeiter())
    print(f'Prozent von Männern zu Frauen: ',c.prozentMaennerzuFrauen(f.Sex.Frau),'%')

if __name__ == '__main__':
    employees = [f.Person(), f.Person(), f.Person(), f.Mitarbeiter(), f.Mitarbeiter(), f.Mitarbeiter(),
                 f.Gruppenleiter(), f.Gruppenleiter(), f.Gruppenleiter()]
    c = Company()
    c.add_persons(employees)
    ausgabe()
