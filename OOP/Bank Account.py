class Conta:

    def __init__(self, num_conta, saldo):
        self.__num_conta = num_conta
        self.__saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor não pode ser 0')

    def saque(self, valor):
        if  self.__saldo >= valor:
            self.__saldo -= valor
            print('Operação realizada com sucesso!')
        else:
            print('Saldo insuficiente!')

    def transferencia(self, destino, valor):
            self.saque(valor)
            destino.deposito(valor)
 
    def saldo(self):
        print(f'Saldo R$ {self.__saldo}')

    def mostrar_num_conta(self):
        return f' {self.__num_conta}'

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

class Cliente(Conta):
    def __init__(self, num_conta, saldo, nome, cpf, rg, cidade):
        super().__init__(num_conta, saldo)
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__cidade = cidade
    
    def info_pessoa(self):
        print(f'Nome: {self.__nome}\nCPF: {self.__cpf}\nRG: {self.__rg}\nCidade: {self.__cidade}\nNúmero da Conta{self.mostrar_num_conta()}\n')

    @property
    def nome(self):
        return self.__nome


cliente1 = Cliente(num_conta=1, saldo=100, nome="Joe", cpf="123.456.789.91", rg="12.345.678-9", cidade="Cidade Qualquer")
cliente2 = Cliente(num_conta=2, saldo=100, nome="Mary", cpf="321.654.987.19", rg="21.543.876-0", cidade="Outra Cidade Qualquer")
cliente3 = Cliente(num_conta=3, saldo=200, nome="John", cpf="221.554.887.99", rg="11.443.776-1", cidade="Outra Cidade Qualquer")
clientes = [cliente1, cliente2, cliente3]

def mostra_clientes(clientes):
    for cliente in clientes:
        print(cliente.info_pessoa())

nome = str(input("Digite o nome: "))
cliente4 = Cliente(num_conta=4, saldo=100, nome=nome, cpf="221.554.887.99", rg="11.443.776-1", cidade="Outra Cidade Qualquer")
print(cliente4.nome)