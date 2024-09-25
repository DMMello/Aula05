
print ("\n[1]Sacar \n[2]Extrato \n[3]Area PIX \n[4]Débito Automatico \n[0}Sair: \n")
opcao = int(input('Resposta: '))
match opcao:
    case 1:
        print("Sacando...")
    case 2:
        print("Exibindo o extrato...")
    case 3:
        print("Area PIX")
    case 4:
        print("Débito Automatico")
    case _:
        print("Erro")


        