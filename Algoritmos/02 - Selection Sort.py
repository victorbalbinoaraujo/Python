def selection_sort(lista):
    for j in range(len(lista) - 1):
        min_index = j
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            lista[j], lista[min_index] = lista[min_index], lista[j]


lista = [3, 6, 1, 4, 6, 1, 5, 8, 9, 3, 1]

selection_sort(lista)
print(lista)