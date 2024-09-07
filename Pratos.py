class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.ingredientes = []

    def exibir_prato(self):
        print(f"Prato: {self.nome}\nPreço: {self.preco}")
        for ingrediente in self.ingredientes:
            print(f"{ingrediente}")


class Pedido:
    def __init__(self, mesa):
        self.pratos = []
        self.mesa = mesa

    def adicionar_prato(self, prato):
        self.pratos.append(prato)
        print(f"Prato {prato.nome} adicionado ao pedido")

    def remover_prato(self, prato):
        if prato in self.pratos:
            self.pratos.remove(prato)
            print(f"Prato {prato.nome} removido do pedido")
        else:
            print(f"{prato.nome} não encontrado nos pedidos")

    def calcular_valor_total(self):
        total = sum(prato.preco for prato in self.pratos)
        print(f"O valor total do pedido é: {total} Mts")

    def mostrar_pedidos(self):
        for prato in self.pratos:
            print(f"Prato: {prato.nome}")


class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.pedidos = []

    def adicionar_pedidos(self, pedido):
        self.pedidos.append(pedido)
        print(f"O pedido da mesa {pedido.mesa} foi adicionado à lista de pedidos")

    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            print(f"Mesa {pedido.mesa}:")
            pedido.mostrar_pedidos()


# Pratos existentes

prato_1 = Prato("Hambúrguer", 550)
prato_1.ingredientes.extend(["hambúrguer", "queijo", "ovo"])

# Pedidos feitos
pedido = Pedido(20)
pedido.adicionar_prato(prato_1)

restaurante = Restaurante("Café Acácias", "Museu")
restaurante.adicionar_pedidos(pedido)
restaurante.mostrar_pedidos()
pedido.calcular_valor_total()
