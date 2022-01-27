import random

if __name__ == "__main__":
    class VerketteteListe:
        def __init__(self):
            self.len = 0
            self.head = None

        def add(self, nValue):
            if self.head:
                lValue = self.head
                while lValue != None:
                    if lValue.nextValue == None:
                        break
                    lValue = lValue.nextValue  
                lValue.nextValue = nValue
            else:
                self.head = nValue

        def returnAll(self):
            if self.head:
                print(self.head.wert)
                temp = self.head
                while temp.nextValue != None:
                    temp = temp.nextValue
                    print(temp.wert)

        def returnLength(self):
            self.len = 0
            if self.head != None:
                self.len += 1
                temp = self.head
                while temp.nextValue != None:
                    self.len += 1
                    temp = temp.nextValue
                print(self.len)

class Daten:
    def __init__(self, wert=0):
        self.wert = wert
        self.nextValue = None


d1 = Daten(random.randint(0, 10))
d2 = Daten(random.randint(0, 10))
d3 = Daten(random.randint(0, 10))

v1 = VerketteteListe()
v1.add(d1)
v1.add(d2)
v1.add(d3)

v1.returnAll()
v1.returnLength()
