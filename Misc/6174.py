def list_to_number(lst):
    s = ''.join(map(str, lst))
    return s

n = int(input("Digite um número de 4 algarismos distintos: "))
num = list(map(int, str(n)))

verify_duplicates = set(num)
contains_duplicates = len(num) != len(verify_duplicates)

i = 1
if len(num) == 4 and contains_duplicates == False:
    while True:
        x = sorted(num)
        y = sorted(num, reverse=True)
        x = list_to_number(x)
        y = list_to_number(y)
        
        resultado = int(y) - int(x)
        print(resultado)
        # Não pode ir além porque 7641 - 1467 é igual a 6174, resultando em um loop infinito após 7 vezes.
        if resultado != 6174:
            num = list(map(int, str(resultado)))
            i += 1
        else:
            print(f"Número de vezes: {i}")
            break