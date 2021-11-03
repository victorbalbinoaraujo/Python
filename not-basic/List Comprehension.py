even_numbers = [x for x in range(10) if x % 2 == 0]
odd_numbers = [x for x in range(10) if x % 2 == 1]
square_list = [x * x for x in range(10)]
even_squares = [x * x for x in even_numbers]
odd_squares = [x * x for x in odd_numbers]
years = [x for x in range(1900, 2010, 10)]
squares_dict = {x: x * x for x in range(11)}
squares_set = {x * x for x in [3, 7, 5, 9, 2]}
pairs = [(x, y)
         for x in range(4)
         for y in range(4)]
increasing_pairs = [(x, y)
                    for x in range(4)
                    for y in range(x + 1, 4)]

list1 = [int(input()) for x in range(5)]
for i, item in enumerate(list1):
    print(f"{i}: {item}")

list2 = [float(input()) for x in range(10)]
list2.reverse()
print(list2)

list3 = [float(input()) for x in range(4)]
media = 0
for x in list3:
    print(x)
    media += x
print(media / 4)

list4 = [int(input()) for x in range(20)]
maior = max(list4)
menor = min(list4)
print(maior)
print(menor)

list5 = [4, 20, 13, 5, 2, 7, 91, 134, 561, 220, 1912, 76, 324, 643, 1245, 6, 2452, 111, 908, 123467]
even = [x for x in list5 if x % 2 == 0]
odd = [x for x in list5 if x % 2 == 1]
print(even)
print(odd)

avg_temp = [float(input()) for x in range(12)]
month = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
annual = 0
for x in avg_temp:
    annual += x
annual /= 12
print(annual)
for i, item in enumerate(avg_temp):
    if item > annual:
        print(f"{i + 1} - {month[i]}")

list_l = [float(input()) for x in range(10)]
list_l2 = [x * 2 for x in list_l]
print(list_l2)

questions = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
             "Tinha dívidas com a vítima?", "Já trabalhou com a vítima?"]
positives = ['S', 'SIM', 'POSITIVO', 'SI', 'YES', 'YEAH', 'AHAM', 'É', 'AFIRMATIVO', 'CERTO', 'ISSO', 'COM CERTEZA',
             'DE ACORDO', 'EFETIVAMENTE', 'CLARO', 'JÁ', 'TINHA', 'MORO', 'ESTIVE', 'TELEFONEI']
score = 0

for x in questions:
    print(x)
    answer = str(input()).upper()
    if answer in positives:
        score += 1
if score == 2:
    print('Suspeita')
elif score == 3 or score == 4:
    print('Cúmplice')
elif score == 5:
    print('Assassino')
else:
    print('Inocente')
