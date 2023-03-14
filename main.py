

#	Реализовать алгоритм пирамидальной сортировки (HeapSort).
#
def heapify(array, size, root):
    indexMax = root
    leftDoughter = 2 * root + 1
    rightDoughter = 2 * root + 2

    if leftDoughter < size and array[leftDoughter] > array[indexMax]:
        indexMax = leftDoughter
    if rightDoughter < size and array[rightDoughter] > array[indexMax]:
        indexMax = rightDoughter
    if indexMax != root:
        array[indexMax], array[root] = array[root], array[indexMax]
        heapify(array, size, indexMax)


initArray = [5, 2, 8, 1, 7, 0, 2]

print(initArray)

for i in range(len(initArray) - 1, -1, -1):
    heapify(initArray, len(initArray), i)

for i in range(len(initArray) - 1, -1, -1):
    initArray[i], initArray[0] = initArray[0], initArray[i]
    heapify(initArray, i, 0)

print(initArray)
