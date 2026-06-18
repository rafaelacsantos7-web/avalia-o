#Mayara Nunes

import modRH as rh
import financeiro as finança
import operacional as operação
import estoque_estudo as estoque


def menuPrincipal(): #menu princiapal que permite escolher ao modelo o usuario qyer acessar
    while True:
       print("\n" + "*"*15 + " BEM-VINDO AO SISTEMA DE CONTROLE DA CARANGOS S/A " + "*"*15)
       print("\nSelecione a opção desejada")

       op = input("digite para:\n 1 - Operacional \n 2 - Estoque \n 3 - Financeiro \n 4 - Recursos Humanos \n 0 - Sair\n")
          
       if op == '1':
          
          operação.op()

       elif op == '2':
          estoque.estoque()

       elif op == '3':
            finança.financeiro()

       elif op == '4':
            rh.menurh()

       elif op == '0':
            print('saindo do sistema....ate logo')
        
       else:
            print('opção invalida. tente novamente')

menuPrincipal()