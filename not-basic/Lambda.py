def square_def(num): return num ** 2


# Atribuir uma função simples a uma variável

square_lambda = lambda num: num ** 2

print(square_def(3))
print(square_lambda(3))

even = lambda num: num % 2 == 0
test = [even(x) for x in range(5)]  # 0 1 2 3 4
print(test)  # T F T F T

first_char = lambda c: c[0]
print(first_char("Lambda"))

invert_string = lambda c: c[::-1]
print(invert_string("String invertida"))

one_to_five_char = lambda c: c[1:5]
print(one_to_five_char("Knights of Cydonia"))

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

print(add(5, 3))
print(subtract(14, 2))
print(multiply(4, 5))
print(divide(9, 2))

media_ponderada = lambda x, y: ((x * 4) + (y * 6)) / 10


def conceito(medias):
    conceitos = []
    for i in medias:
        if i < 4.9:
            conceitos.append("D")
        elif 5 <= i <= 6.9:
            conceitos.append("C")
        elif 7.0 <= i <= 8.9:
            conceitos.append("B")
        elif 9.0 <= i <= 10.0:
            conceitos.append("A")
    return conceitos


turma = []
for i in range(10):
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = media_ponderada(nota1, nota2)
    turma.append(media)

conceito(turma)

prestacao = lambda financ, prazo, taxa: financ * (((1 + taxa) ** prazo) * taxa) / (((1 + taxa) ** prazo) - 1)


def percentual(prazo):
    if prazo == 6:
        perc = 0.07 / 12
    elif prazo == 12:
        perc = 0.10 / 12
    elif prazo == 18:
        perc = 0.12 / 12
    elif prazo == 24:
        perc = 0.15 / 12
    elif prazo == 36:
        perc = 0.18 / 12
    return perc


valor_financiamento = float(input("Valor do financiamento: "))
while valor_financiamento != -1:
    prazo = int(input("Digite o valor do prazo: "))
    taxa = percentual(prazo)
    p = prestacao(valor_financiamento, prazo, taxa)
    print(f"Prestação do financiamento: {p}")
    valor_financiamento = float(input("Valor do financiamento: "))

maior = lambda a, b: a if a > b else b
test1 = maior(12, 7)
test2 = maior(7, 12)

dezoito = lambda a: print("Maior de idade") if a >= 18 else print("Menor de idade")
dezoito(5)
dezoito(22)

c_to_f = lambda x: (x * (9 / 5)) + 32
f_to_c = lambda x: (x - 32) * 5 / 9
k_to_c = lambda x: x - 273.15
c_to_k = lambda x: x + 273.15
f_to_k = lambda x: ((x - 32) * 5 / 9) + 273.15
k_to_f = lambda x: (x - 273.15) * 9 / 5 + 32

import random

numeros = list(range(20))
numeros = random.sample(numeros, 10)
print(numeros)

pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

import random

mpf = lambda: print("Minha primeira função!")
mpf()

nome_idade = lambda nome, idade: print(f"{nome} possui {idade} anos")
nome_idade("Victor", 20)

maiores = lambda x: x > 10
numeros = [random.randrange(50) for _ in range(5)]
print(numeros)
nums_maiores_que_10 = filter(maiores, numeros)
print(list(nums_maiores_que_10))
