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
    def __init__(self, Abteilung=Abteilung.einkauf, Sex=Sex.Mann):
        self.Abteilung = Abteilung
        self.Sex = Sex


class Mitarbeiter(Person):
    def __init__(self, dep: Abteilung = Abteilung.produktion, sex: Sex = Sex.Frau):
        super().__init__(dep, sex)


class Gruppenleiter(Mitarbeiter):
    def __init__(self, dep: Abteilung = Abteilung.verkauf, sex: Sex = Sex.Mann):
        super().__init__(dep, sex)
