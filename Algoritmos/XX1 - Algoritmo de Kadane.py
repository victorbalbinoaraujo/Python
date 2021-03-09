def kadane(lista):
    max_sum = current_sum = lista[0]

    for i in lista[1:]:
        current_sum = max(current_sum+i, i)
        max_sum = max(max_sum, current_sum)

    return max_sum


lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(kadane(lista))