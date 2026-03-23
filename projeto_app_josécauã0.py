'''

CRUD 

BARBEARIA

Atender o cliente com responsabilidade e cortar o cabelo do cliente ser atencioso e respeitoso.
'''

print("\n=== GESTÃO DA BARBEARIA ===")
print("1. Agendar Corte")
print("2. Ver Agenda do Dia")
print("3. Alterar Horário")
print("4. Cancelar Agendamento")
print("5. Cadastrar Cliente")
print("6. Listar Clientes")
print("7. Remover Cliente")
print("8. Serviços Disponíveis")
print("9. Relatório Financeiro")
print("0. Sair") 

escolha = input("Escolha uma opção: ")

while True: 
    if escolha == '1':
        print("Agendar Corte...") 
    # código para agendar corte 1
     
    elif escolha == '2': 
         print("ver agenda do dia ")
    # código para ver agenda do dia  2
    elif escolha == '3':
        print("alterar horário")
    # código para alterar horário 3
    elif escolha == '4':
        print("cancelar agendamento")
    # código para cancelar agendamento 4
    elif escolha == '5':
        print("cadastrar cliente")
    # código para cadastrar cliente  5
    elif escolha == '6':
        print("listar clientes")
    # código para  6
    elif escolha == '7':
        print("remover cliente ")
    # código para agendar corte 7
    elif escolha == '8':
        print("serviços disponíveis ")
    # código para agendar corte 8
    elif escolha == '9':
        print("relatório financeiro")
    # código para agendar corte 9
    elif escolha == '0':
       print("Sair") 
       break
    # código para agendar corte 0

else:
    print("Opção inválida. por favor, tente novamente. ") 