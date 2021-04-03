import random

# A função zip cria um objeto que une as duas listas criando tuplas entre seus elementos.
# Tuplas compostas por primeiro valor de list1 com primeiro valor de list2 e assim por diante.
# Zip leva em consideração a lista que contém a MENOR quantidade de elementos.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]
zip1 = zip(list1, list2)

print(zip1)
#zip1 é um objeto no momento, é necessário transformá-lo em uma lista para visualizar melhor os seus elementos.
list_zip = list(zip1)
print(list_zip)
# Como zip utiliza a lista com menor número de elementos, o elemento 4 da list2 não é mostrado.

# Unzip
# Para realizar a operação de unzip, é necessário criar duas novas tuplas e utilizar o * com o zip em forma de lista
# Para criar 2 listas que contém os elementos.
list3, list4 = zip(*list_zip)
print(list3)
print(list4) # Como o elemento 4 não está no list_zip, ele também não vai estar no list4.

nomes = ['Abigail', 'Breno', 'Caique', 'Danilo']
salarios = [random.randrange(1100, 10000) for _ in range(4)]
idades = [random.randrange(18,65) for _ in range(4)]

m_salario = 0
m_idade = 0
for n, s, i in zip(nomes, salarios, idades):
    if s > m_salario:
        m_salario = s
        nm_salario = n
    if i > m_idade:
        m_idade = i
        nm_idade = n
        
print(f"{nm_salario} tem o maior salário: R${m_salario},00")
print(f"{nm_idade} é a pessoa mais velha com {m_idade} anos.")