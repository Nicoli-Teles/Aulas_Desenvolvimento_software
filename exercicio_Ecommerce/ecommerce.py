import uuid

class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Cliente:
    """ Representa um cliente do e-commerce, associado a uma pessoa. atributos: pessoa, id_cliente"""
    def __init__(self, pessoa: Pessoa):
        self.pessoa = pessoa
        self.id_cliente = str(uuid.uuid4())

class Produto:
    """ Representa um produto disponível para venda. atributos: nome, preco, estoque"""
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class ItemPedido:
    """ Representa um item dentro de um pedido. Contém um produto, quantidade e estoque após o pedido. atributos: produto, quantidade, estoque_após_pedido"""
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.estoque_após_pedido = produto.estoque - quantidade  # Armazena o estoque após o pedido

    def calcular_total(self):
        return self.produto.preco * self.quantidade

class Pedido:
    """ Representa um pedido realizado por um cliente. Contém o cliente e uma lista de itens. atributos: cliente, itens"""
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item: ItemPedido):
        if item.produto.estoque >= item.quantidade:
            self.itens.append(item)
            item.produto.estoque -= item.quantidade  # Diminui o estoque do produto
            print(f'Adicionado {item.quantidade} de {item.produto.nome} ao pedido.')
        else:
            print(f'O produto: {item.produto.nome} está sem estoque suficiente. Estoque atual: {item.produto.estoque}')

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.calcular_total()  # Usa o método calcular_total do ItemPedido
        return total

class Menu:
    """ Gerencia o e-commerce, permitindo o cadastro de clientes, produtos e pedidos. atributos: clientes, produtos, pedidos"""
    def __init__(self):
        self.clientes = {}
        self.produtos = {}
        self.pedidos = []

    def cadastrar_cliente(self, nome, cpf, email):
        if cpf not in self.clientes:
            pessoa = Pessoa(nome, cpf, email)
            cliente = Cliente(pessoa)
            self.clientes[cpf] = cliente
            print(f'Cliente {nome} cadastrado com sucesso!')
        else:
            print('O CPF informado já está vinculado a um cadastro')

    def cadastrar_produto(self, nome, preco, estoque):
        if nome not in self.produtos:
            preco = float(preco)
            estoque = int(estoque)
            produto = Produto(nome, preco, estoque)
            self.produtos[nome] = produto
            print(f'Produto {nome} cadastrado com sucesso')
        else:
            print('Este produto já foi cadastrado')

    def criar_pedido(self, cpf):
        if cpf in self.clientes:
            pedido = Pedido(self.clientes[cpf])
            print('Pedido criado com sucesso!')
            return pedido
        else:
            print("Cliente não encontrado.")
            return None

    def visualizar_pedidos(self):
        if not self.pedidos:
            print("Nenhum pedido encontrado.")
            return
        for pedido in self.pedidos:
            print(f"\nPedido do cliente {pedido.cliente.pessoa.nome}:")
            for item in pedido.itens:
                print(f" - {item.produto.nome}: {item.quantidade} unidades (Estoque após o pedido: {item.estoque_após_pedido})")
            print(f"Total: R${pedido.calcular_total():.2f}")

    def exibir_menu(self):
        while True:
            print("\n" + "═" * 40)
            print("🌟  BEM-VINDO AO MENU DO E-COMMERCE  🌟")
            print("═" * 40 + "\n")
            print("📋  1. Cadastrar Cliente")
            print("🛒  2. Cadastrar Produto")
            print("📦  3. Criar Pedido")
            print("📜  4. Visualizar Pedidos")
            print("🚪  5. Sair")
            print("═" * 40 + "\n")
    
            escolha = input("Escolha uma opção (1-5): ")

            if escolha == "1":
                nome = input('Insira o nome do cliente: ')
                cpf = input('Insira o cpf do cliente: ')
                email = input('Insira o email do cliente: ')
                self.cadastrar_cliente(nome, cpf, email)
            elif escolha == "2":
                nome = input('Insira o nome do produto: ')
                preco = input('Insira o preço do produto (em reais): ')
                estoque = input('Insira a quantidade de estoque do produto: ')
                self.cadastrar_produto(nome, preco, estoque)
            elif escolha == "3":
                cpf = input('Digite o CPF do cliente: ')
                cliente_encontrado = self.clientes.get(cpf)
                if cliente_encontrado:
                    pedido = Pedido(cliente_encontrado)
                    while True:
                        produto_nome = input('Digite o nome do produto ou (sair) para finalizar o pedido: ')
                        if produto_nome in self.produtos:
                            quantidade = int(input("Digite a quantidade: "))
                            item = ItemPedido(self.produtos[produto_nome], quantidade)
                            pedido.adicionar_item(item)
                        elif produto_nome.lower() == 'sair':
                            break
                        else:
                            print('Desculpe, produto não encontrado!')
                    self.pedidos.append(pedido)  # Adiciona o pedido à lista de pedidos
                else:
                    print("O CPF solicitado não está cadastrado!")
            elif escolha == "4":
                self.visualizar_pedidos()
            elif escolha == '5':
                print('Saindo do sistema...')
                break
            else:
                print('Opção inválida. Por favor, escolha um número entre 1 e 5')

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()