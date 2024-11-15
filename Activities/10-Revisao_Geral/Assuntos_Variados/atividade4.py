pacientes = {}

for i in range(3):
    print(f"\n{i+1}° Paciente")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")
    sintomas = input("Sintomas: ")

    confirmacao = input("\nOs dados informados estão corretos? [s/n]\n-> ").lower()

    if(confirmacao == 's'):
        infos = {'idade': idade, 'email': email, 'sintomas': sintomas }
        pacientes[nome] = infos
        continue
    
    else:
        while(confirmacao != 's'):
            print(f"\n{i+1}° Paciente")
            nome = input("Nome: ")
            idade = input("Idade: ")
            email = input("Email: ")
            sintomas = input("Sintomas: ")

            confirmacao = input("\nOs dados informados está corretos? [s/n]\n-> ").lower()
        
        infos = {'idade': idade, 'email': email, 'sintomas': sintomas }
        pacientes[nome] = infos

print("\nInformações dos Pacientes\n")

for paciente in pacientes:
    print(f"Paciente: {paciente}")
    print(f"Idade: {pacientes[paciente]['idade']}")
    print(f"Email: {pacientes[paciente]['email']}")
    print(f"Sintomas: {pacientes[paciente]['sintomas']}\n")
