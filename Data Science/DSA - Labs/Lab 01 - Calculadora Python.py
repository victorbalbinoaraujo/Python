def menu():

    print(20 * "*", "Python Calculator", 20 * "*")
    print("""
    Selecione o número da operação desejada:

    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão

     """)
    
def operations(op, x, y): return {
    1 : lambda: x + y,
    2 : lambda: x - y,
    3 : lambda: x * y,
    4 : lambda: x / y,
}.get(op, lambda:"Opção inválida") ()

symbols = {
    1 : '+',
    2 : '-',
    3 : '*',
    4 : '/'
}

menu()

op = int(input("Digite sua opção (1/2/3/4): "))

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print(f"{x} {symbols[op]} {y} = {operations(op, x, y)}")