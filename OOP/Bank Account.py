class Conta:

    def __init__(self, num_conta, saldo):
        self.num_conta = num_conta
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor não pode ser 0')

    def saque(self, valor):
        if  self.saldo >= valor:
            self.saldo -= valor
            print('Operação realizada com sucesso!')
        else:
            print('Saldo insuficiente!')

    def transferencia(self, destino, valor):
            self.saque(valor)
            destino.deposito(valor)
 
    def mostrar_saldo(self):
        print(f'Saldo R$ {self.saldo}')

class Cliente(Conta):
    def __init__(self, num_conta, saldo, nome, cpf, rg, cidade):
        super().__init__(num_conta, saldo)
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cidade = cidade


conta1 = Conta(num_conta=1, saldo=150)
conta2 = Conta(num_conta=2, saldo=90)

conta1.transferencia(conta2, 30)
conta2.mostrar_saldo()





