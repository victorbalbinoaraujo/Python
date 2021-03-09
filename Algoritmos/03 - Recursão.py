def imprime_linha():
    print('linha 1')
    imprime_texto()
    print('linha 2')

def imprime_texto():
    print('texto')

imprime_linha()
#linha 1
#texto
#linha 2

def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(5))
#120

