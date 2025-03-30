import unittest
from io import StringIO
import sys

from ecommerce import Pessoa, Cliente, Produto, ItemPedido, Pedido, Menu

class TestEcommerce(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste antes de cada teste."""
        self.menu = Menu()
        self.cliente1 = Pessoa("João Silva", "12345678901", "joao@email.com")
        self.cliente2 = Pessoa("Maria Oliveira", "98765432100", "maria@email.com")
        self.produto1 = Produto("Produto A", 10.00, 100)
        self.produto2 = Produto("Produto B", 20.00, 50)

        # Cadastrando clientes e produtos para os testes
        self.menu.cadastrar_cliente(self.cliente1.nome, self.cliente1.cpf, self.cliente1.email)
        self.menu.cadastrar_cliente(self.cliente2.nome, self.cliente2.cpf, self.cliente2.email)
        self.menu.cadastrar_produto(self.produto1.nome, self.produto1.preco, self.produto1.estoque)
        self.menu.cadastrar_produto(self.produto2.nome, self.produto2.preco, self.produto2.estoque)

    def test_cadastrar_cliente(self):
        """Testa o cadastro de um cliente."""
        self.assertIn(self.cliente1.cpf, self.menu.clientes)
        self.assertIn(self.cliente2.cpf, self.menu.clientes)

    def test_cadastrar_produto(self):
        """Testa o cadastro de um produto."""
        self.assertIn(self.produto1.nome, self.menu.produtos)
        self.assertIn(self.produto2.nome, self.menu.produtos)

    def test_criar_pedido(self):
        """Testa a criação de um pedido."""
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        self.assertIsNotNone(pedido)
        self.assertEqual(pedido.cliente.pessoa.nome, self.cliente1.nome)

    def test_adicionar_item_pedido(self):
        """Testa a adição de itens a um pedido."""
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item = ItemPedido(self.produto1, 2)
        pedido.adicionar_item(item)
        self.assertEqual(len(pedido.itens), 1)
        self.assertEqual(pedido.itens[0].quantidade, 2)

    def test_calcular_total_pedido(self):
        """Testa o cálculo do total de um pedido."""
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item1 = ItemPedido(self.produto1, 2)  # 2 unidades de Produto A
        item2 = ItemPedido(self.produto2, 1)  # 1 unidade de Produto B
        pedido.adicionar_item(item1)
        pedido.adicionar_item(item2)
        total = pedido.calcular_total()
        self.assertEqual(total, (2 * self.produto1.preco) + (1 * self.produto2.preco))

    def test_visualizar_pedidos(self):
        """Testa a visualização de pedidos."""
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item = ItemPedido(self.produto1, 2)
        pedido.adicionar_item(item)
        self.menu.pedidos.append(pedido)  # Adiciona o pedido à lista de pedidos

        # Redireciona a saída padrão para capturar a impressão
        captured_output = StringIO()
        sys.stdout = captured_output

        self.menu.visualizar_pedidos()
        sys.stdout = sys.__stdout__  # Restaura a saída padrão

        # Verifica se a saída contém informações do pedido
        self.assertIn("Pedido do cliente João Silva:", captured_output.getvalue())
        self.assertIn("Produto A: 2 unidades", captured_output.getvalue())
        self.assertIn(f"Total: R${pedido.calcular_total():.2f}", captured_output.getvalue())

    def test_adicionar_item_pedido(self):
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item = ItemPedido(self.produto1, 2)
        pedido.adicionar_item(item)
        self.assertEqual(len(pedido.itens), 1)
        self.assertEqual(pedido.itens[0].produto.nome, "Produto A")

    def test_cadastrar_cliente(self):
        self.assertIn(self.cliente1.cpf, self.menu.clientes)
        self.assertIn(self.cliente2.cpf, self.menu.clientes)

    def test_cadastrar_produto(self):
        self.assertIn(self.produto1.nome, self.menu.produtos)
        self.assertIn(self.produto2.nome, self.menu.produtos)

    def test_calcular_total_pedido(self):
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item1 = ItemPedido(self.produto1, 2)
        item2 = ItemPedido(self.produto2, 1)
        pedido.adicionar_item(item1)
        pedido.adicionar_item(item2)
        total = pedido.calcular_total()
        self.assertEqual(total, 40.0)  # 2 * 10 + 1 * 20

    def test_criar_pedido(self):
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        self.assertIsNotNone(pedido)
        self.assertEqual(pedido.cliente.pessoa.nome, "João Silva")

    def test_visualizar_pedidos(self):
        pedido = self.menu.criar_pedido(self.cliente1.cpf)
        item = ItemPedido(self.produto1, 2)
        pedido.adicionar_item(item)
        self.menu.pedidos.append(pedido)
        self.menu.visualizar_pedidos()  # Deve imprimir os detalhes do pedido

    def tearDown(self):
        """Limpa o ambiente de teste após cada teste."""
        self.menu = None


if __name__ == "__main__":
    unittest.main()