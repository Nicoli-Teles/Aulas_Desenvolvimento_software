class Cliente:  # pode realizar muitas transações
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta: 'Conta'): # as aspas são usadas para indicar type uma boa pratica em python
        self.contas.append(conta) #uma adição simples de lista

    def realizar_transacao(self, conta: 'Conta', transacao: 'Transacao'):
        if not self.contas: #verifica se a lista de contas está vazia
            print("Você não tem uma conta.")
            return
        if conta not in self.contas: #verifica se o cliente possui uma conta na lista que ja possui contas registradas
            print("Conta não associada ao cliente.")
            return
        
        # Tenta registrar a transação
        transacao.registrar(conta) #chamada de metodo da classe transação
        
        # Adiciona a transação ao histórico apenas se for um depósito ou se o saque foi bem-sucedido
        if isinstance(transacao, Deposito) or (isinstance(transacao, Saque) and conta.saldo >= transacao.valor): #verifica se é deposito ou saque --> isinstace (se é uma instancia)
            conta.historico.adicionar_transacao(transacao) 
        else:
            print("Transação não registrada no histórico devido a falha.")


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Transacao:  # um histórico pode ter várias transações
    def registrar(self, conta: 'Conta'):
        pass  # Método a ser implementado nas subclasses


class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: 'Conta'):
        conta.saldo += self.valor
        print(f"Depósito de {self.valor} realizado na conta.")


class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: 'Conta'):
        if self.valor > conta.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            conta.saldo -= self.valor
            print(f"Saque de {self.valor} realizado na conta.")


class Historico:  # só pode ter um histórico por conta
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)
        print("Transação adicionada ao histórico.")


class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def obter_saldo(self) -> float:
        return self.saldo

    def nova_conta(self, cliente: Cliente, numero: int) -> 'Conta':
        nova_conta = Conta(0.0, numero, self.agencia, cliente)
        cliente.adicionar_conta(nova_conta)
        return nova_conta

    def sacar(self, valor: float) -> bool:
        if valor > self.saldo:
            print("Saque não realizado. Saldo insuficiente.")
            return False
        self.saldo -= valor
        print(f"Saque de {valor} realizado com sucesso.")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de depósito deve ser positivo.")
            return False
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso.")
        return True


############################################################# zona de teste ########################################################
def Teste():
    # criar cliente
    cliente1 = PessoaFisica(endereco="Rua das Flores, 123", cpf="123.456.789-00", nome="João Silva", data_nascimento="01/01/1990")
    
    # Criar conta corrente para o cliente
    conta1 = Conta(saldo=1000.0, numero=1, agencia="001", cliente=cliente1)
    cliente1.adicionar_conta(conta1)

    # Exibe saldo inicial
    print(f"Saldo inicial da conta: {conta1.obter_saldo()}")

    # Realiza um depósito
    deposito = Deposito(valor=500.0)
    cliente1.realizar_transacao(conta1, deposito)

    # Exibe saldo após depósito
    print(f"Saldo após depósito: {conta1.obter_saldo()}")

    # Realiza saque
    saque = Saque(valor=300.0)
    cliente1.realizar_transacao(conta1, saque)

    # Exibindo saldo após saque
    print(f"Saldo após saque: {conta1.obter_saldo()}")

    # Tentando realizar um saque maior que o saldo
    saque_invalido = Saque(valor=1500.0)
    cliente1.realizar_transacao(conta1, saque_invalido)

    # Exibindo saldo final
    print(f"Saldo final da conta: {conta1.obter_saldo()}")

    # Exibindo histórico de transações
    print("Histórico de transações:")
    for transacao in conta1.historico.transacoes:
        if isinstance(transacao, Deposito):
            print(f"Depósito: {transacao.valor}") 
        elif isinstance(transacao, Saque):
            print(f"Saque: {transacao.valor}")
 
if __name__ == "__main__":
    Teste()