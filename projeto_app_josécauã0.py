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

escolha = input("escolha uma opção ")

while True: 
    if escolha == '1':
        print("Agendar Corte...") 
     
    elif escolha == '2': 
         print("ver agenda do dia ")
    
    elif escolha == '3':
        print("alterar horário")
    
    elif escolha == '4':
        print("cancelar agendamento")
    
    elif escolha == '5':
        print("cadastrar cliente")

    elif escolha == '6':
        print("listar clientes")
    
    elif escolha == '7':
        print("remover cliente ")
    
    elif escolha == '8':
        print("serviços disponíveis ")
    
    elif escolha == '9':
        print("relatório financeiro")
    
    elif escolha == '0':
       print("Sair") 
       break

# CREATE - Agendar corte
    if escolha == '1':
        print("\n--- Agendar Corte ---")
        for i, c in enumerate(clientes):
            print(f"{i} - {c['nome']}")

        indice = int(input("Escolha o cliente: "))
        servico = input("Serviço (corte/barba/corte e barba): ").lower()

        valor = tabela_precos.get(servico, 0)

        if valor > 0:
            clientes[indice]["servico"] = servico
            clientes[indice]["valor"] = valor
            print(">> Agendamento realizado!")
        else:
            print(">> Serviço inválido!")

    # READ - Ver agenda
    elif escolha == '2':
        print("\n--- Agenda do Dia ---")
        for c in clientes:
            if c["servico"]:
                print(f"{c['nome']} - {c['servico']}")

    # UPDATE - Alterar serviço
    elif escolha == '3':
        print("\n--- Alterar Serviço ---")
        for i, c in enumerate(clientes):
            print(f"{i} - {c['nome']}")

        indice = int(input("Escolha o cliente: "))
        novo_servico = input("Novo serviço: ").lower()

        valor = tabela_precos.get(novo_servico, 0)

        if valor > 0:
            clientes[indice]["servico"] = novo_servico
            clientes[indice]["valor"] = valor
            print(">> Serviço atualizado!")
        else:
            print(">> Serviço inválido.")

    # DELETE - Cancelar agendamento
    elif escolha == '4':
        print("\n--- Cancelar Agendamento ---")
        for i, c in enumerate(clientes):
            print(f"{i} - {c['nome']}")

        indice = int(input("Escolha o cliente: "))

        clientes[indice]["servico"] = None
        clientes[indice]["valor"] = 0.0

        print(">> Agendamento cancelado!")

    # CREATE - Cadastrar cliente
    elif escolha == '5':
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        cliente = {
            "nome": nome,
            "telefone": telefone,
            "servico": None,
            "valor": 0.0
        }

        clientes.append(cliente)
        print(">> Cliente cadastrado!")