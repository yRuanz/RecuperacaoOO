class Banco:
    def __init__(self, nomeB, endereco):
        self.nomeB = nomeB
        self.endereco = endereco
        self.clientes = {}


    #Este método deve criar uma conta bancária com o nome do titular e o saldo inicial especificado.
    def Criar_conta(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial

    #Este método deve permitir que o titular da conta especificada retire uma quantia de dinheiro igual ao valor fornecido. Certifique-se de que haja saldo suficiente na conta para efetuar o saque.
    def Sacar(self, conta, valor):
        self.conta = [self.nome, self.saldo_inicial]
        self.valor = valor

    #Este método deve permitir que o titular da conta especificada deposite uma quantia de dinheiro igual ao valor fornecido. Certifique-se de que o valor informado, seja um valor positivo.
    def Depositar(self, conta, valor):
        self.conta = [self.nome, self.saldo_inicial]
        self.valor = valor

    #Este método deve permitir a transferência de dinheiro da conta de origem para a conta de destino, com o valor especificado. Certifique-se de que haja saldo suficiente na conta de origem para efetuar a transferência.
    def Transferir(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor

    #Este método deve retornar o saldo atual da conta especificada.    
    def Saldo(self, conta):
        self.conta = [self.nome, self.saldo_inicial]

