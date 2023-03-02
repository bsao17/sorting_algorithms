from random import randint

l = [5, 8, 10, 2, 1]


def selectionSort(l):
    for unsorted_index in range(0, len(l)):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index + 1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min
    print(l)


def generateRandomListSorted(nbr, min, max):
    l = []
    for i in range(nbr):
        l.append(randint(min, max))
    selectionSort(l)


generateRandomListSorted(15, 2, 25)
