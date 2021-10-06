def bubblesort(nlist):
    n = len(nlist)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]

def insertionsort(nlist):
    for i in range(1, len(nlist)):
        key = nlist[i]
        j = i - 1
        while j >= 0 and key < nlist[j]:
            nlist[j + 1] = nlist[j]
            j -= 1
        nlist[j + 1] = key


def selectionsort(nlist):
    for i in range(len(nlist)):
        min = i
        for j in range(i + 1, len(nlist)):
            if nlist[min] > nlist[j]:
                min = j
        nlist[i], nlist[min] = nlist[min], nlist[i]


if __name__ == '__main__':
    nlist = [1, 4, 3, 5, 7, 8, 0, 9, 2]
    bubblesort(nlist)
    print(nlist)
    nlist = [1, 4, 3, 5, 7, 8, 0, 9, 2]
    insertionsort(nlist)
    print(nlist)
    nlist = [1, 4, 3, 5, 7, 8, 0, 9, 2]
    selectionsort(nlist)
    print(nlist)