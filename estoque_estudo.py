#Rafaela Santos
def estoque():
    import os
    import json

    # Criar arquivo
    def criar_arquivo(nome_do_arquivo):
        if not os.path.exists(nome_do_arquivo):
            with open(nome_do_arquivo, "w") as arquivo:
                json.dump([], arquivo)

    # Ler arquivo
    def ler_arquivo(nome_do_arquivo):
        with open(nome_do_arquivo, "r") as arquivo:
            return json.load(arquivo) 

    # Salva dados
    def salvar_dados(dados, nome_do_arquivo):
        with open(nome_do_arquivo, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

    # Limprar dados
    def limpar_dados(nome_do_arquivo):
        with open(nome_do_arquivo, "w") as arquivo:
            json.dump([], arquivo)

    # Criando arquivo de produtos
    criar_arquivo("produtos.json")
    criar_arquivo("json.json")

    def cadastrar_produto():
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        data_fabricacao = input("Data de Fabricação (dd/mm/aaaa): ")
        fornecedor = input("Digite o nome do fornecedor: ")
        qtd_produtos = int(input("Digite a quantidade de produtos: "))
        valor_compra = float(input("Digite o valor de compra: "))

        # Ler arquivo de produtos
        produtos = ler_arquivo("produtos.json")

        # Verifica se o produto já existe
        for produto in produtos:
            if produto["codigo"] == codigo:
                print("Produto já cadastrado!")
                return

        # Cria o dicionário do produto
        produto = {
            "codigo": codigo,
            "nome": nome,
            "data_fabricacao": data_fabricacao,
            "fornecedor": fornecedor,
            "quantidade": qtd_produtos,
            "valor_compra": valor_compra
        }

        # Adiciona produto à lista
        produtos.append(produto)

        # Salva lista de produtos
        salvar_dados(produtos, "produtos.json")
        
        print("Produto cadastrado com sucesso!")



    def buscar_produto(codigo, produtos):
        for produto in produtos:
            if produto["codigo"] == codigo:
                return produto
        return None

    def calcular_produto(produtos):
        print("\nCÁLCULO DE CUSTOS")
        print("=" * 50)

        for produto in produtos:
            quantidade = produto['quantidade']
            valor = produto['valor_compra']

            #  fórmula base
            valor_total = quantidade * valor

            # calculos
            valor_semanal = valor_total * 7
            valor_mensal = valor_total * 30
            valor_anual = valor_total * 365

            print("-" * 40)
            print(f"Produto: {produto['nome']}")
            print(f"Valor total estoque: R$ {valor_total:.2f}")
            print(f"Semanal: R$ {valor_semanal:.2f}")
            print(f"Mensal: R$ {valor_mensal:.2f}")
            print(f"Anual: R$ {valor_anual:.2f}")


    def listar_produtos(produtos):
        print("\nLISTAGEM DE PRODUTOS")
        print("=" * 50)

        for produto in produtos:
            print("-" * 40)
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Data: {produto['data_fabricacao']}")
            print(f"Fornecedor: {produto['fornecedor']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Valor de Compra: R$ {produto['valor_compra']:.2f}")


    # ---------------- MENU ----------------
    def menu():
        while True:
            print("\n===== MENU =====")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Calcular custos")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_produto()

            elif opcao == "2":
                produtos = ler_arquivo("produtos.json")
                listar_produtos(produtos)

            elif opcao == "3":
                produtos = ler_arquivo("produtos.json")
                calcular_produto(produtos)

            elif opcao == "4":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida!")


    # EXECUÇÃO
    menu()