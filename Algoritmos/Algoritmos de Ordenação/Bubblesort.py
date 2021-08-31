def bubblesort(lista):
    lista_len = len(lista)
    for i in range(lista_len - 1):
        for j in range(lista_len - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                


lista = [1, 5, 22, 77, 24, 28, 2, 62, 21, 3, 7]

print(f"""
      Lista não ordenada para teste
      {lista}
      """)

bubblesort(lista)

print(f"""
      Lista após a aplicação do Bubblesort
      {lista}
      """)

input()