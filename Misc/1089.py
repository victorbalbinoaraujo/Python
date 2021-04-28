def inverter(num):
    inversao = list(map(int, str(num)))
    inversao.reverse()
    inversao = list_to_number(inversao)
    return inversao

def list_to_number(lst):
    s = ''.join(map(str, lst))
    s = int(s)
    return s

n = int(input("Digite um número com três algarismos distintos: "))

# Invertendo número
num1 = inverter(n)

# Realizando subtração
sub = num1 - n if num1 > n else n - num1
sub1 = inverter(sub)

