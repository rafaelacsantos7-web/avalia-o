#Mayara Nunes

# Lista principal onde ficam armazenados os dados dos funcionários
funcionarios = [
    {
        "nome": "João Silva",
        "cpf": "123.456.789-00",
        "rg": "12.345.678-9",
        "endereco": "Rua A, 100 - Salvador/BA",
        "telefone": "(71) 99999-1111",
        "cargo": "operador de producao",
        "qtd_filhos": 2
    },
    {
        "nome": "Maria Santos",
        "cpf": "234.567.890-11",
        "rg": "23.456.789-0",
        "endereco": "Rua B, 200 - Salvador/BA",
        "telefone": "(71) 99999-2222",
        "cargo": "auxiliar administrativo",
        "qtd_filhos": 1
    },
    {
        "nome": "Carlos Oliveira",
        "cpf": "345.678.901-22",
        "rg": "34.567.890-1",
        "endereco": "Rua C, 300 - Salvador/BA",
        "telefone": "(71) 99999-3333",
        "cargo": "gerente de producao",
        "qtd_filhos": 3
    },
    {
        "nome": "Ana Souza",
        "cpf": "456.789.012-33",
        "rg": "45.678.901-2",
        "endereco": "Rua D, 400 - Salvador/BA",
        "telefone": "(71) 99999-4444",
        "cargo": "inspetor de qualidade",
        "qtd_filhos": 0
    },
    {
        "nome": "Pedro Lima",
        "cpf": "567.890.123-44",
        "rg": "56.789.012-3",
        "endereco": "Rua E, 500 - Salvador/BA",
        "telefone": "(71) 99999-5555",
        "cargo": "diretor operacional",
        "qtd_filhos": 4
    }
]

# Tabela de cargos e valor da hora de trabalho de cada um
cargos = {
    "presidente executivo": 120.00,
    "diretor operacional": 80.00,
    "diretor financeiro": 80.00,
    "diretor de rh": 80.00,
    "gerente de producao": 50.00,
    "gerente de suprimentos": 50.00,
    "gerente financeiro": 50.00,
    "gerente de rh": 50.00,
    "auxiliar administrativo": 18.00,
    "auxiliar de servicos gerais": 15.00,
    "montador de veiculos": 25.00,
    "inspetor de qualidade": 30.00,
    "operador logistico": 22.00,
    "operador de producao": 20.00
}


# Menu principal do sistema. Ele fica repetindo até o usuário escolher sair.
def menurh():

    while True:

        print("\n" + "*" * 15 + " SISTEMA DE RECURSOS HUMANOS DA CARANGOS S/A " + "*" * 15)
        print("\nSelecione a opção desejada:")

        op1 = input(
            "Digite:\n"
            "1 - Cadastro de funcionários\n"
            "2 - Cálculo do salário\n"
            "3 - Cálculo de horas extras\n"
            "4 - Cálculo de IRPF\n"
            "5 - Geração de relatório completo\n"
            "0 - Sair\n"
        )

        if op1 == '1':
            cadastro_funcionarios(funcionarios)

        elif op1 == '2':
            calculo_salario(funcionarios)

        elif op1 == '3':
            calculo_horas_extras(funcionarios)

        elif op1 == '4':
            calculo_irpf(funcionarios)

        elif op1 == '5':
            relatorio_completo(funcionarios)

        elif op1 == '0':
            print("Saindo do sistema... até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função responsável pelo CRUD dos funcionários (Cadastrar, Consultar, Alterar e Excluir e ver funcionarios cadastrados).

def cadastro_funcionarios(funcionarios):

    while True:

        print("\n===== CADASTRO DE FUNCIONÁRIOS =====")
        print("1 - Ver funcionários")
        print("2 - Cadastrar funcionário")
        print("3 - Alterar funcionário")
        print("4 - Excluir funcionário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        # READ - Ler / Consultar
        if opcao == "1":

            print("\n===== LISTA DE FUNCIONÁRIOS =====")

            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for i, funcionario in enumerate(funcionarios, start=1):
                    print(f"\nFuncionário {i}")
                    print("Nome:", funcionario["nome"])
                    print("CPF:", funcionario["cpf"])
                    print("RG:", funcionario["rg"])
                    print("Endereço:", funcionario["endereco"])
                    print("Telefone:", funcionario["telefone"])
                    print("Cargo:", funcionario["cargo"].title())
                    print("Qtd. Filhos:", funcionario["qtd_filhos"])

        # CREATE - Criar
        elif opcao == "2":

            while True:

                print("\n===== NOVO FUNCIONÁRIO =====")

                print("\n=== CARGOS DISPONÍVEIS ===")

                lista_cargos = list(cargos.keys())

                for i, cargo in enumerate(lista_cargos, start=1):
                    print(f"{i} - {cargo.title()}")

                nome = input("\nNome: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")

                opcao_cargo = int(input("Selecione o número do cargo: "))

                if opcao_cargo < 1 or opcao_cargo > len(lista_cargos):
                    print("Cargo inválido!")
                    continue

                cargo = lista_cargos[opcao_cargo - 1]

                qtd_filhos = int(input("Quantidade de filhos: "))

                novo_funcionario = {
                    "nome": nome,
                    "cpf": cpf,
                    "rg": rg,
                    "endereco": endereco,
                    "telefone": telefone,
                    "cargo": cargo,
                    "qtd_filhos": qtd_filhos
                }

                funcionarios.append(novo_funcionario)

                print("Funcionário cadastrado com sucesso!")

                resposta = input(
                    "\nDeseja cadastrar outro funcionário? (S/N): "
                ).strip().upper()

                if resposta != "S":
                    break

        # UPDATE - Atualizar / Alterar
        elif opcao == "3":

            print("\n===== ALTERAR FUNCIONÁRIO =====")

            for i, funcionario in enumerate(funcionarios, start=1):
                print(f"{i} - {funcionario['nome']}")

            indice = int(input("Digite o número do funcionário: ")) - 1

            if 0 <= indice < len(funcionarios):

                print("\n=== CARGOS DISPONÍVEIS ===")

                lista_cargos = list(cargos.keys())

                for i, cargo in enumerate(lista_cargos, start=1):
                    print(f"{i} - {cargo.title()}")

                funcionarios[indice]["nome"] = input("Novo nome: ")
                funcionarios[indice]["cpf"] = input("Novo CPF: ")
                funcionarios[indice]["rg"] = input("Novo RG: ")
                funcionarios[indice]["endereco"] = input("Novo endereço: ")
                funcionarios[indice]["telefone"] = input("Novo telefone: ")

                opcao_cargo = int(input("Selecione o número do novo cargo: "))

                if 1 <= opcao_cargo <= len(lista_cargos):
                    funcionarios[indice]["cargo"] = lista_cargos[opcao_cargo - 1]
                else:
                    print("Cargo inválido!")

                funcionarios[indice]["qtd_filhos"] = int(
                    input("Nova quantidade de filhos: ")
                )

                print("Funcionário atualizado com sucesso!")

            else:
                print("Funcionário não encontrado!")

        # DELETE - Excluir / Apagar
        elif opcao == "4":

            print("\n===== EXCLUIR FUNCIONÁRIO =====")

            for i, funcionario in enumerate(funcionarios, start=1):
                print(f"{i} - {funcionario['nome']}")

            indice = int(
                input("Digite o número do funcionário que deseja excluir: ")
            ) - 1

            if 0 <= indice < len(funcionarios):

                removido = funcionarios.pop(indice)

                print(
                    f"Funcionário {removido['nome']} removido com sucesso!"
                )

            else:
                print("Funcionário não encontrado!")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

# Faz o cálculo completo do salário, incluindo horas extras e IRPF.
def calculo_salario(funcionarios):

    while True:

        print("\n===== CÁLCULO DE SALÁRIO =====")

        cpf = input("Digite o CPF do funcionário: ")

        funcionario = None

        for f in funcionarios:
            if f["cpf"] == cpf:
                funcionario = f
                break

        if funcionario is None:
            print("Funcionário não encontrado!")

            resposta = input(
                "\nDeseja calcular outro salário? (S/N): "
            ).strip().upper()

            if resposta != "S":
                break

            continue

        cargo = funcionario["cargo"]

        valor_hora = cargos[cargo]

        print("\n===== DADOS DO FUNCIONÁRIO =====")
        print("Nome:", funcionario["nome"])
        print("Cargo:", cargo.title())
        print(f"Valor da Hora: R$ {valor_hora:.2f}")

        horas_trabalhadas = float(
            input("\nQuantidade de horas trabalhadas no mês: ")
        )

        salario_base = valor_hora * horas_trabalhadas

        valor_horas_extras = 0

        total_horas_50 = 0
        total_horas_100 = 0

        valor_horas_50 = 0
        valor_horas_100 = 0

        # Presidente, diretores e gerentes não recebem hora extra
        if (
            cargo != "presidente executivo"
            and "diretor" not in cargo
            and "gerente" not in cargo
        ):

            while True:

                resposta = input(
                    "\nDeseja lançar horas extras para este funcionário? (S/N): "
                ).upper()

                if resposta != "S":
                    break

                horas_extras = float(
                    input("Quantidade de horas extras: ")
                )

                tipo_dia = input(
                    "\nAs horas extras foram realizadas em:\n"
                    "1 - Segunda a sábado\n"
                    "2 - Domingo/Feriado\n"
                    "Escolha: "
                )

                # Domingo ou feriado = 100%
                if tipo_dia == "2":

                    total_horas_100 += horas_extras

                    valor = horas_extras * (valor_hora * 2)

                    valor_horas_100 += valor
                    valor_horas_extras += valor

                    print(
                        f"{horas_extras} hora(s) lançadas com adicional de 100%."
                    )

                # Segunda a sábado
                else:

                    passou_duas_horas = input(
                        "Neste dia foram ultrapassadas 2 horas extras? (S/N): "
                    ).upper()

                    if passou_duas_horas == "N":

                        total_horas_50 += horas_extras

                        valor = horas_extras * (valor_hora * 1.5)

                        valor_horas_50 += valor
                        valor_horas_extras += valor

                        print(
                            f"{horas_extras} hora(s) lançadas com adicional de 50%."
                        )

                    else:

                        horas_50 = min(2, horas_extras)
                        horas_100 = max(0, horas_extras - 2)

                        total_horas_50 += horas_50
                        total_horas_100 += horas_100

                        valor50 = horas_50 * (valor_hora * 1.5)
                        valor100 = horas_100 * (valor_hora * 2)

                        valor_horas_50 += valor50
                        valor_horas_100 += valor100

                        valor_horas_extras += valor50 + valor100

                        print(
                            f"{horas_50} hora(s) calculadas a 50%."
                        )
                        print(
                            f"{horas_100} hora(s) calculadas a 100%."
                        )

        else:
            print("Este cargo não possui direito a horas extras.")

        salario_bruto = salario_base + valor_horas_extras

        # Cálculo do IRPF
        if salario_bruto <= 5000:

            irpf = 0

        elif salario_bruto <= 7350:

            imposto_base = (salario_bruto * 0.275) - 908.73

            redutor = 978.62 - (0.133145 * salario_bruto)

            irpf = imposto_base - redutor

            if irpf < 0:
                irpf = 0

        else:

            irpf = (salario_bruto * 0.275) - 908.73

        salario_liquido = salario_bruto - irpf

        print("\n===== RESUMO DO SALÁRIO =====")

        print(f"Funcionário: {funcionario['nome']}")
        print(f"CPF: {funcionario['cpf']}")
        print(f"Cargo: {cargo.title()}")
        print(f"Valor da Hora: R$ {valor_hora:.2f}")
        print(f"Horas Trabalhadas: {horas_trabalhadas}")

        if valor_horas_extras > 0:

            print("\n===== DETALHAMENTO DAS HORAS EXTRAS =====")

            print(f"Horas a 50%: {total_horas_50}")
            print(f"Valor das Horas a 50%: R$ {valor_horas_50:.2f}")

            print(f"Horas a 100%: {total_horas_100}")
            print(f"Valor das Horas a 100%: R$ {valor_horas_100:.2f}")

            print(f"Total de Horas Extras: R$ {valor_horas_extras:.2f}")

        print(f"\nSalário Base: R$ {salario_base:.2f}")
        print(f"Salário Bruto: R$ {salario_bruto:.2f}")
        print(f"IRPF: R$ {irpf:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

        funcionario["horas_trabalhadas"] = horas_trabalhadas
        funcionario["salario_bruto"] = salario_bruto
        funcionario["irpf"] = irpf
        funcionario["salario_liquido"] = salario_liquido

        resposta = input(
            "\nDeseja calcular outro salário? (S/N): "
        ).strip().upper()

        if resposta != "S":
            break

# Calcula somente as horas extras do funcionário selecionado.
def calculo_horas_extras(funcionarios):

    print("\n===== CÁLCULO DE HORAS EXTRAS =====")

    cpf = input("Digite o CPF do funcionário: ")

    funcionario = None

    for f in funcionarios:
        if f["cpf"] == cpf:
            funcionario = f
            break

    if funcionario is None:
        print("Funcionário não encontrado!")
        return

    cargo = funcionario["cargo"]

    print(f"\nFuncionário: {funcionario['nome']}")
    print(f"Cargo: {cargo.title()}")

    # Presidente, diretores e gerentes não recebem horas extras
    if (
        cargo == "presidente executivo"
        or "diretor" in cargo
        or "gerente" in cargo
    ):
        print("Este cargo não possui direito a horas extras.")
        return

    valor_hora = cargos[cargo]

    print(f"Valor da Hora: R$ {valor_hora:.2f}")

    total_horas_50 = 0
    total_horas_100 = 0

    valor_horas_50 = 0
    valor_horas_100 = 0

    valor_total_horas_extras = 0

    while True:

        horas_extras = float(
            input("\nQuantidade de horas extras: ")
        )

        tipo_dia = input(
            "\nAs horas extras foram realizadas em:\n"
            "1 - Segunda a sábado\n"
            "2 - Domingo/Feriado\n"
            "Escolha: "
        )

        # Domingo ou feriado = 100%
        if tipo_dia == "2":

            total_horas_100 += horas_extras

             # Hora extra em domingo ou feriado vale 100%, ou seja, o dobro da hora normal
            valor = horas_extras * (valor_hora * 2)

            valor_horas_100 += valor
            valor_total_horas_extras += valor

            print(
                f"\n{horas_extras} hora(s) lançadas com adicional de 100%."
            )

        # Segunda a sábado
        else:

            passou_duas_horas = input(
                "Neste dia foram ultrapassadas 2 horas extras? (S/N): "
            ).upper()

            if passou_duas_horas == "N":

                total_horas_50 += horas_extras

                 # Hora extra comum recebe adicional de 50%, por isso multiplicamos por 1.5
                valor = horas_extras * (valor_hora * 1.5)

                valor_horas_50 += valor
                valor_total_horas_extras += valor

                print(
                    f"\n{horas_extras} hora(s) lançadas com adicional de 50%."
                )

            else:
                # As primeiras 2 horas ficam com adicional de 50%

                horas_50 = min(2, horas_extras)
                # Tudo o que passar de 2 horas recebe adicional de 100%
                horas_100 = max(0, horas_extras - 2)

                total_horas_50 += horas_50
                total_horas_100 += horas_100

                valor50 = horas_50 * (valor_hora * 1.5)
                valor100 = horas_100 * (valor_hora * 2)

                valor_horas_50 += valor50
                valor_horas_100 += valor100

                valor_total_horas_extras += valor50 + valor100

                print("\n===== DETALHAMENTO DO LANÇAMENTO =====")
                print(f"Horas a 50%: {horas_50}")
                print(f"Valor das Horas a 50%: R$ {valor50:.2f}")
                print(f"Horas a 100%: {horas_100}")
                print(f"Valor das Horas a 100%: R$ {valor100:.2f}")

        continuar = input(
            "\nDeseja lançar mais horas extras para este funcionário? (S/N): "
        ).upper()

        if continuar != "S":
            break

    print("\n===== RELATÓRIO FINAL DE HORAS EXTRAS =====")

    print(f"Funcionário: {funcionario['nome']}")
    print(f"CPF: {funcionario['cpf']}")
    print(f"Cargo: {cargo.title()}")
    print(f"Valor da Hora Normal: R$ {valor_hora:.2f}")

    print("\n===== RESUMO =====")

    print(f"Total de Horas a 50%: {total_horas_50}")
    print(f"Valor Total das Horas a 50%: R$ {valor_horas_50:.2f}")

    print(f"Total de Horas a 100%: {total_horas_100}")
    print(f"Valor Total das Horas a 100%: R$ {valor_horas_100:.2f}")

    print(
        f"\nValor Total das Horas Extras: R$ {valor_total_horas_extras:.2f}"
    )

# Calcula o IRPF com base no salário bruto informado.
def calculo_irpf(funcionarios):

    while True:
        print("\n===== CÁLCULO DE IRPF =====")

        cpf = input("Digite o CPF do funcionário: ")
        funcionario = None

        for f in funcionarios:
            if f["cpf"] == cpf:
                funcionario = f
                break

        if funcionario is None:
            print("Funcionário não encontrado!")
        else:
            cargo = funcionario["cargo"]
            valor_hora = cargos[cargo]
            horas_trabalhadas = float(input("Quantidade de horas trabalhadas no mês: "))

            salario_bruto = valor_hora * horas_trabalhadas

            # Regras de IRPF
            if salario_bruto <= 5000:
                irpf = 0
            elif salario_bruto <= 7350:
                imposto_base = (salario_bruto * 0.275) - 908.73
                redutor = 978.62 - (0.133145 * salario_bruto)
                irpf = imposto_base - redutor
                if irpf < 0:
                    irpf = 0
            else:
                irpf = (salario_bruto * 0.275) - 908.73

            salario_liquido = salario_bruto - irpf

            print("\n===== RESUMO DO IRPF =====")
            print(f"Funcionário: {funcionario['nome']}")
            print(f"Cargo: {cargo.title()}")
            print(f"Salário Bruto: R$ {salario_bruto:.2f}")

            if irpf == 0:
                print("Este funcionário não paga IRPF.")
            else:
                print(f"Este funcionário paga R$ {irpf:.2f} de IRPF.")

            print(f"Salário Líquido: R$ {salario_liquido:.2f}")

            funcionario["horas_trabalhadas"] = horas_trabalhadas
            funcionario["salario_bruto"] = salario_bruto
            funcionario["irpf"] = irpf
            funcionario["salario_liquido"] = salario_liquido

        # Pergunta ao usuário se deseja continuar
        opcao = input("\nDeseja calcular o IRPF de outro funcionário? (S/N): ").strip().lower()

        if opcao != "s":
            print("Encerrando cálculo de IRPF...")
            break

def relatorio_completo(funcionarios):
    print("\n===== RELATÓRIO COMPLETO =====")

    funcionarios_ordenados = sorted(funcionarios, key=lambda f: f["nome"])

    # Ordena os funcionários pelo nome
    for funcionario in funcionarios_ordenados:

        cargo = funcionario["cargo"]
        valor_hora = cargos[cargo]

        if "salario_bruto" in funcionario:

            salario_bruto = funcionario["salario_bruto"]
            irpf = funcionario["irpf"]
            salario_liquido = funcionario["salario_liquido"]
            horas_trabalhadas = funcionario["horas_trabalhadas"]

        else:
            # Considerando 220 horas/mês
            horas_trabalhadas = 220
              # Calculando o salário bruto
            salario_bruto = valor_hora * horas_trabalhadas

            if salario_bruto <= 5000:

                irpf = 0

            elif salario_bruto <= 7350:

                imposto_base = (salario_bruto * 0.275) - 908.73
                redutor = 978.62 - (0.133145 * salario_bruto)
                irpf = imposto_base - redutor

                if irpf < 0:
                    irpf = 0

            else:

                irpf = (salario_bruto * 0.275) - 908.73

            salario_liquido = salario_bruto - irpf

        print("\n-----------------------------------")
        print(f"Funcionário: {funcionario['nome']}")
        print(f"Cargo: {cargo.title()}")
        print(f"Horas Trabalhadas: {horas_trabalhadas}")
        print(f"Salário Bruto: R$ {salario_bruto:.2f}")
        print(f"IRPF: R$ {irpf:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")

        if irpf == 0:
            print("Este funcionário não paga IRPF.")
        else:
            print(f"Este funcionário paga R$ {irpf:.2f} de IRPF.")    
   