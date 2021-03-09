def binary_search(lista, item, begin=0, end=None):
    if end is None:
        end = len(lista) - 1
    if begin <= end:
        middle = (begin + end) // 2
        if lista[middle] == item:
            return middle
        if item < lista[middle]:
            return binary_search(lista, item, begin, middle - 1)
        else:
            return binary_search(lista, item, middle + 1, end)
    return None

lista1 = [1, 2, 5, 7, 9, 12, 16, 19, 21]

print(binary_search(lista1, 7))