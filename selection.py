from random import randint


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
    print(f"sorted list: {l}")


def generateRandomListSorted(nbr, min, max):
    l = []
    for i in range(nbr):
        l.append(randint(min, max))
    print(f"unsorted list: {l}")
    selectionSort(l)


generateRandomListSorted(10, 2, 15)
