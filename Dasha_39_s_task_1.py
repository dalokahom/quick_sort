from random import choice


def sortNumbers(array):
    dividedByThreeNumbers = list(filter(lambda e: e % 3 == 0, array))
    notDividedByThreeNumbers = list(filter(lambda e: e % 3 != 0, array))
    return qsort(dividedByThreeNumbers) + qsort(notDividedByThreeNumbers)

def qsort(array):
    if not array: return array
    pivot = array[choice(range(0, len(array)))]

    head = qsort([elem for elem in array if elem < pivot])
    tail = qsort([elem for elem in array if elem > pivot])
    return head + [elem for elem in array if elem == pivot] + tail


numbersArray = list(map(int, input("Ведите числа, которые нужно отсортировать, через пробел:").split()))
sortedArray = sortNumbers(numbersArray)
print(*sortedArray, sep = ', ')
