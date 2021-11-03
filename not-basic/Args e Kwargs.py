# Args é uma palavra genérica (convenção) para utilizar em uma função múltiplos parâmetros.
# Na realidade o *variável é uma tupla.
def exemplo_args(*params):
    print(max(params)) # Neste caso imprime o maior argumento.

exemplo_args('d', 'b', 'c', 'a') # Imprime d
exemplo_args(4, 7, 8, 1) # Imprime 8


# Kwargs segue o mesmo princípio do args com a diferença que é necessário nomear os argumentos na chamada de função.
# Na realidade **variável é um dicionário.
def exemplo_kwargs(**params):
    for key, value in params.items():
        print(f"{key.capitalize()}: {value}")

exemplo_kwargs(texto="Texto", numero=10) # Imprime texto Texto numero 10
exemplo_kwargs(nome="Fulano", idade="42", cpf="123.456.789.00", esporte="Futebol")
# Qualquer nome é válido.

# Desempacotar valores.
dicionario = {
    "chave1" : "valor1",
    "chave2" : "valor2"
}

def desempacotar(chave1, chave2):
    print("chave1", chave1)
    print("chave2", chave2)

desempacotar(**dicionario)