class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = float(saldo) 
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def imprimir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta = Conta("João Silva", "123.456.789-00", "0001254", 100)

conta.depositar(150)

conta.sacar(100)

conta.sacar(200)

conta.imprimir_saldo()
