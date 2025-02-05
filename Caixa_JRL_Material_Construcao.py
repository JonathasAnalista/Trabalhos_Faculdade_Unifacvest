class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} - Estoque: {self.quantidade}"

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
        else:
            self.produtos[nome] = Produto(nome, preco, quantidade)

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    def exibir_estoque(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            print("\nEstoque atual:")
            for produto in self.produtos.values():
                print(produto)

class Caixa:
    def __init__(self, estoque):
        self.estoque = estoque
        self.vendas = []

    def registrar_venda(self, nome, quantidade):
        if nome in self.estoque.produtos:
            if self.estoque.produtos[nome].quantidade >= quantidade:
                self.estoque.remover_produto(nome, quantidade)
                total = self.estoque.produtos[nome].preco * quantidade
                self.vendas.append((nome, quantidade, total))
                print(f"Venda registrada: {quantidade} de {nome} - Total: R${total:.2f}")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    def exibir_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
        else:
            print("\nVendas registradas:")
            for venda in self.vendas:
                print(f"Produto: {venda[0]}, Quantidade: {venda[1]}, Total: R${venda[2]:.2f}")

def main():
    print("Bem-vindo ao JRL Material de Construção!")
    estoque = Estoque()
    caixa = Caixa(estoque)

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Exibir Estoque")
        print("4. Registrar Venda")
        print("5. Exibir Vendas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            estoque.adicionar_produto(nome, preco, quantidade)
            print("Produto adicionado com sucesso.")

        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a remover: "))
            estoque.remover_produto(nome, quantidade)

        elif opcao == '3':
            estoque.exibir_estoque()

        elif opcao == '4':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a vender: "))
            caixa.registrar_venda(nome, quantidade)

        elif opcao == '5':
            caixa.exibir_vendas()

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()