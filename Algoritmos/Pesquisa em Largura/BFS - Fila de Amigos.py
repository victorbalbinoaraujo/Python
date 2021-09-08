from collections import deque

grafo = {}

grafo["Alex"] = ["Bob", "Claire", "Daniel"]
grafo["Bob"] = ["Claire", "Erik"]
grafo["Claire"] = ["Erik"]
grafo["Daniel"] = ["Fernando"]
grafo["Erik"] = ["Fernando"]
grafo["Fernando"] = []


def disponivel_festa(pessoa):
    return pessoa[0] == "E"

def bfs(nome):
    fila_pesquisa = deque()
    fila_pesquisa += grafo[nome]
    verificadas = []
    while fila_pesquisa:
        pessoa = fila_pesquisa.popleft()
        if not pessoa in verificadas:
            if disponivel_festa(pessoa):
                print(f"{pessoa} está disponível para a festa! 😀")
                return True
        else:
            fila_pesquisa += grafo[pessoa]
    return False

bfs("Alex")

        