import random
import time

import LinkedList as li
import ArrayList as al

if __name__ =="__main__":
    llist = li.LinkedList()
    arr = al.ArrayarrList()
    for i in range(10000):
        arr.addItem(random.randint(0,10))
        llist.addNode(random.randint(0,10))


    start = time.time()
    arr.sortASC()
    end = time.time()
    print("Zeit ArrayList: ",end-start, "Sekunden")

    startArr = time.time()
    llist.sortListASC()
    endArr = time.time()
    print("Zeit LinkedList", endArr-startArr, "Sekunden")

