import random # Preencher as listas aleatoriamente para gerar diferentes resultados.
from functools import reduce # Para reduce, última função.

# Map
# Utiliza determinada função em um conjunto de dados.
list1 = [random.randrange(0,101) for _ in range(5)]

def plus_two(x):
    return x + 2

def double(x):
    return 2 * x


map1 = map(plus_two, list1)
map2 = map(double, list1)
list_map1 = list(map1)
list_map2 = list(map2)
print("Map")
print(f"Lista 1: {list1}")
print(f"Função plus two: {list_map1}") # Neste caso, somamos cada elemento da lista por 2 como dita a função plus_two.
print(f"Função double: {list_map2}") # Neste caso, multiplicamos cada elemento da lista por 2 como dita a função double.


# É possível passar múltiplos argumentos se fornecer múltiplas listas.
list2 = [random.randrange(0,10) for _ in range(3)]
list3 = [random.randrange(0,10) for _ in range(3)]

def multiply(x, y):
    return x * y

def sum(x, y):
    return x + y

map3 = map(multiply, list2, list3)
map4 = map(sum, list2, list3)
list_map3 = list(map3)
list_map4 = list(map4)
print(f"Lista 2: {list2}")
print(f"Lista 3: {list3}")
print(f"Função multiply: {list_map3}")
print(f"Função sum: {list_map4}\n\n\n")

# Filter
# Utiliza determinada função condicional em um conjunto de dados.
# Diferente de map, filter apenas aceita 2 argumentos, a função e a lista, portanto, não é possível passar 2 ou + listas como argumento.
list4 = [random.randrange(0, 10) for _ in range(5)]

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 == 1

filter1 = filter(is_even, list4)
filter2 = filter(is_odd, list4)
list_filter1 = list(filter1)
list_filter2 = list(filter2)
print("Filter")
print(f"Lista 4: {list4}")
print(f"Função is even: {list_filter1}") # Imprimir todos os elementos pares da lista.
print(f"Função is odd: {list_filter2}\n\n\n") # Imprimir todos os elementos ímpares da lista.


# Reduce
# Reduce combina os elementos de uma lista reduzindo a único elemento, dependendo da função que utilizar.
# É necessário importar reduce dá biblioteca functools
list5 = [random.randrange(1, 10) for _ in range(8)]

# Funções multiply e sum utilizadas no exemplo com map.

reduce1 = reduce(multiply, list5)
reduce2 = reduce(sum, list5)
print("Reduce")
print(f"Lista 5: {list5}")
print(f"Função multiply: {reduce1}") # Todos os números da lista multiplicados.
print(f"Função sum: {reduce2}") # Todos os números da lista somados.
