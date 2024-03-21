from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal


class ContaCorrente(ABC):
    def __init__(self):
        self._saldo = 0
        self._operacoes = []

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaCorrenteMulher(ContaCorrente):
    def __init__(self, clientes):
        super().__init__()
        self.clientes = clientes
        self._cheque_especial = sum(cliente.renda_mensal for cliente in clientes)

    def sacar(self, valor):
        if self._saldo - valor >= -self._cheque_especial:
            self._saldo -= valor
            self._operacoes.append(f"Saque de R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor acima do cheque especial.")

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(f"Depósito de R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")


class ContaCorrenteHomem(ContaCorrente):
    def __init__(self, clientes):
        super().__init__()
        self.clientes = clientes

    def sacar(self, valor):
        if self._saldo - valor >= 0:
            self._saldo -= valor
            self._operacoes.append(f"Saque de R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(f"Depósito de R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")


#exemplos:

cliente_mulher = Cliente("Ana", "123456789", 3000)
cliente_homem = Cliente("João", "987654321", 4000) #criação de clientes


conta_mulher = ContaCorrenteMulher([cliente_mulher])
conta_homem = ContaCorrenteHomem([cliente_homem]) #criação de contas correntes

#operações:
conta_mulher.depositar(500)
conta_mulher.sacar(2000)

conta_homem.depositar(1000)
conta_homem.sacar(1500)
