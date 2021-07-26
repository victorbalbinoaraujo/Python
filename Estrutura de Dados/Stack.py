"""
Pilha / Stack

LIFO

Last in, First Out
(o último a entrar é o primeiro a sair.)

Push(data) -> Adicionar elemento na pilha.

Pop()  -> Remover o topo elemento da pilha.

Size() -> Tamanho da pilha.

Exemplos: 
Ctrl + Z
Guias do Browser (voltar uma página.)
Cálculo de distâncias
Pilha do MTG
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):

        self.items.append(data)

    def size(self):
        return len(self.items)
    
    def pop(self):

        if self.size() == 0:
            return None
        else:
            return self.items.pop()

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3) # Último elemento que foi colocado.

stack.pop() # Removendo o 3

print(stack.items) # [1, 2]