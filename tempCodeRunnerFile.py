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
