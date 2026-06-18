#Kaylanne da Silva dos Santos
def op():

    lista = []

    def cadastro():
        cadastros = 1
        
        while cadastros <= 3:
            print('=.'*30)
            print('=.'*12,'Cadastro','=.'*13)
            print('=.'*30)
        
            turno = input('1- Matutino.\n2- Vespertino.\n3- Noturno.\n')
            if turno == '1':
                turno = 'Matutino'
            elif turno == '2':
                turno = 'Vespertino'
            elif turno == '3':
                turno = 'Noturno'
            else:
                print('Opção Inválida!')
                continue
            while True:
                funcionario = input(f"Informe a quantidade de funcionarios operando no turno '{turno.title()}'.\n")
                if not funcionario.isnumeric():
                    print('Opção inválida!\nUse apenas números!')
                    continue
                funcionario = int(funcionario)
                break
            
            soma_produ = []
            dia = 1
            while dia <= 7:
                try:
                    producao = int(input(f"Informe a quantidade de produção do {dia}° dia do turno '{turno.title()}'.\n"))
                    soma_produ.append(producao)
                    dia +=1

                    soma_semanal = sum(soma_produ)
                    producao = round(sum(soma_produ)/7)
                except ValueError:
                    print('Erro!\nPor favor, Informe números com valor interio!')
        
            dicio = {'turno' : turno,
                    'funcionario' : funcionario,
                    'producao media' : producao,
                    'producao semanal' : soma_semanal
                    }
            lista.append(dicio)
            desejo = input('Deseja continuar o cadastro?\n').lower().strip()
            if 'não' in desejo or 'nao' in desejo or 'n' in desejo:
                break
            cadastros += 1

    def simulacao():
        while True:
            print('=='*30)
            print('              Simulação e Detalhe de Produção')
            print('=='*30)
            
            op = input('\n1- Produção Real.\n2- Produção Ideal.\n3- Comparação de Produção Real e Ideal\n4- Sair\n')
            
            match op:
                case '1':
                    print('=-'*30)
                    print('                      Produção Real')
                    print('=-'*30)
                    
                    producao_media = 0
                    
                    for produtos in lista:
                        print('--'*30)
                        print(f'Turno: {produtos["turno"]}\nQuantidade de Funcionários: {produtos["funcionario"]}\nMédia de Produção: {produtos["producao media"]}')
                        print(f'Quantidade de Produção Semanal {produtos["producao semanal"]}')
                        print('--'*30)
                        
                        producao_media += produtos['producao media']
                        pro_mensal = producao_media * 30
                        pro_anual = producao_media * 365
                        
                    print('-='*30)
                    print(f'Produção mensal de todos os turnos: {pro_mensal}\nProdução Anual de todos os turnos: {pro_anual}')
                    print('-='*30)
                case '2':
                    print('=-'*30)
                    print('                      Produção Ideal')
                    print('=-'*30)
                    turno_1 = 250
                    total_dia = round(turno_1/30)
                    print('-'*53)
                    print(f'Produção Ideal por mês com 1 turno ativo: {turno_1}\nProdução Ideal por dia com 1 turno ativo: {total_dia}')
                    print('-'*53)

                    turno_2 = 500
                    total_dia1 = round(turno_2/30)
                    print('-'*53)
                    print(f'Produção Ideal por mês com 2 turno ativo: {turno_2}\nProdução Ideal por dia com 1 turno ativo: {total_dia1}')
                    print('-'*53)
                    
                    turno_3 = turno_1 + turno_2
                    total_dia2 = round(turno_3/30)
                    print('-'*53)
                    print(f'Produção Ideal por mês com 3 turno ativo: {turno_3}\nProdução Ideal por dia com 1 turno ativo: {total_dia2}')
                    print('-'*53)
                case '3':
                    print('=-'*30)
                    print('             Comparação de Produção Real e Ideal')
                    print('=-'*30)
                    
                    producao_media = 0
                    turno = len(lista)
                    for produtos in lista:
                        producao_media += produtos['producao media']
            
                        pro_mensal = producao_media * 30
                    
                    multi = 2
                    while multi <=3:
                    
            
                        turno_1 = (500 / 100) * 50
                        turno_3 = (turno_1 * 2) + 250 
                        porce_ideal = ((turno_1 * multi) * 100) / turno_3 
                        porce_real = (pro_mensal * porce_ideal) / (turno_1 * multi)
                        print('-'*53)
                        print(f'Produção Ideal mensal com {multi} turno ativo: {turno_1 * multi:.0f} de {porce_ideal:.0f}% \nProdução Real mensal com {turno} turno ativo: {pro_mensal} de {porce_real:.0f}%')
                        print('-'*53)
                        
                        multi += 1 

                case '4':
                    break
                case _:
                    print('Opção Invalida!')
        

    def operacional():    
        while True:
            print('-=-_-'*12)
            print('-=-_'*6,'OPERACIONAL','-=-_'*6)
            print('-=-_-'*12)

            op = input('\n1- Cadastro de turnos.\n2- Simulação e Detanha da produção.\n3- Sair.\n')
            match op:
                case '1':
                    cadastro()
                case '2':
                    print('2')
                    simulacao()
                case '3':
                    print('Encerrando...')
                    break
                case _:
                    print('Opção inexistente!')
    operacional()