import random
import time


class ArrayarrList:
    def __init__(self):
        self.arrList = []

    def addItem(self, item):
        self.arrList.append(item)

    def addItemBefore(self, pos, item):
        if pos < 0:
            return
        elif pos > len(self.arrList):
            return
        else:
            self.arrList.insert(pos-1, item)

    def addItemAfter(self, pos, item):
        if pos < 0:
            return
        elif pos > len(self.arrList):
            return
        else:
            self.arrList.insert(pos + 1, item)

    def removeItemBefore(self, pos):
        if pos < 0:
            return
        elif pos > len(self.arrList):
            return
        else:
            self.arrList.pop(pos-1)

    def removeItemAfter(self, pos):
        if pos < 0:
            return
        elif pos > len(self.arrList):
            return
        else:
            self.arrList.pop(pos + 1)

    def findItem(self, item):
        if item < 0:
            return
        else:
            for i in self.arrList:
                if i == item:
                    index = self.arrList.index(item)
                    print("Position in List",item, ": ", index)
                    return
            print("Not in List")

    def getLength (self):
        return print("Length of List: ", len(self.arrList))

    def sortASC(self):
        for i in range(len(self.arrList)):
            key = self.arrList[i]
            j = i - 1
            while j >= 0 and key < self.arrList[j]:
                self.arrList[j + 1] = self.arrList[j]
                j -= 1
            self.arrList[j + 1] = key

    def sortDESG(self):
        for i in range(len(self.arrList)):
            key = self.arrList[i]
            j = i - 1
            while j >= 0 and key > self.arrList[j]:
                self.arrList[j + 1] = self.arrList[j]
                j -= 1
            self.arrList[j + 1] = key

    def min(self):
        return print("Min: ",min(self.arrList))

    def max(self):
        return print("max: ",max(self.arrList))

    def sum(self):
        return print("Sum of all elements: ",sum(self.arrList))

    def avg(self):
        sumArr = sum(self.arrList)
        return print("Avg: ",sumArr/len(self.arrList))

    def returnArrayarrList(self):
        output = []
        for i in self.arrList:
            output.append(i)
        print(output)



if __name__ == "__main__":
    arr = ArrayarrList()
    for i in range(10):
        arr.addItem(random.randint(0,10))

    # arr.returnArrayarrList()
    arr.addItemBefore(6,600)
    # arr.returnArrayarrList()
    # arr.addItemAfter(6, 600)
    # arr.returnArrayarrList()
    # arr.removeItemAfter(6)
    arr.returnArrayarrList()
    arr.removeItemBefore(6)
    arr.returnArrayarrList()
    # arr.sortDESG()
    # arr.returnArrayarrList()
    start = time.time()
    arr.sortASC()
    end = time.time()
    print(end-start)
    # arr.returnArrayarrList()
    # arr.findItem(1)
    # arr.getLength()
    # arr.min()
    # arr.max()
    # arr.sum()
    # arr.avg()
