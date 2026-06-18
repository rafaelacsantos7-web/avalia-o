#Deivide Bembem
def financeiro():

    while True:
        print("BEM VINDO AO FINANCEIRO")

        print("Vamos ver suas despesas? Primeiro eu preciso que você me diga alguns dados importantes:")

        agua = float(input("\nPor favor me informe o total gasto com a conta de água: "))
        luz= float(input("\nPor favor, me informe o total gasto com a conta de luz: "))
        salario= float(input("\nPor favor, me informe o total gasto com os salários: "))
        imposto= float(input("\nPor favor, me informe o total gasto com as impostos: "))
        carros_produzidos= int(input("Por favor, me informe o total de carros produzidos esse mês: \n"))

        if carros_produzidos <=0:
            print("ERRO ERRO ERRO ESSE MÊS A FÁBRICA NÃO PRODUZIU CARROS")
            print("Só posso te ajudar a calcular o valor dos carros quando tiver carros a serem produzidos, por favor me informe um mês que foi produzido carros.")
            continue
            


        despesas= agua+luz+salario+imposto
        valor_custo=despesas/carros_produzidos
        valor_carro= valor_custo*1.5
        lucro_por_carro= valor_carro-valor_custo
        lucro_total= lucro_por_carro*carros_produzidos

        print(f"Todas as suas despesas esse mês deu um valor de : {despesas:.2f}")
        print(F"Cada carro custou o valor de: {valor_custo:.2f}")
        print(f"O valor médio dos carros é de: {valor_carro:.2f}")
        print(f"O lucro que você teve por carro é de: {lucro_por_carro :.2f}")
        print(f"O lucro que você teve esse mês foi de:  {lucro_total:.2f}")
        break
