from enum import Enum


class Sex(Enum):
    Indeterminable = 0,
    Mann = 1,
    Frau = 2


class Abteilung(Enum):
    keineAbteilung = 0,
    einkauf = 1,
    produktion = 2,
    verkauf = 3,


class Person():
    def __init__(self, vorname, name, sex, abteilung):
        self.vorname = vorname
        self.name = name
        self.Abteilung = abteilung
        self.Sex = sex


class Mitarbeiter(Person):
    def __init__(self, vorname, name, sex, abteilung, gehalt):
        super().__init__(vorname, name, sex, abteilung)
        self.Gehalt = gehalt


class Gruppenleiter(Mitarbeiter):
    def __init__(self, vorname, name, sex, abteilung, gehalt, id):
        super().__init__(vorname, name, sex, abteilung, gehalt)
        self.Id = id
