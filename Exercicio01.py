import os
os.system("cls")

# num = int(input('Escreve um número entre 1 e 12 :'))
# match num:
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 4:
#         print("Abril")
#     case 5:
#         print("Maio")
#     case 6:
#         print("Junho")
#     case 7:
#         print("Julho")
#     case 8:
#         print("Agosto")
#     case 9:
#         print("Setembro")
#     case 10:
#         print("Outubro")
#     case 13:
#         print("Novembro")
#     case 12:
#         print("Dezembro")
#     case _:
#         print("Mês não encontrado")
     



# print ("\n[1]Japonês \n[2]Italiano \n[3]Mexicano \n[4]Vegetariano\n")
# opcao = int(input('Resposta: '))
# match opcao:
#     case 1:
#         print("Você escolheu a comida Japonesa.\nTemos um excelente combo de harumaki + hot (10 unid)")
#     case 2:
#         print("Você escolheu um prato Italiano. \nQue tal uma carbonara?")
#     case 3:
#         print("Você escolheu um prato mexicano. \nQue tal umas tortilhas?")
#     case 4:
#         print("Excelente escolha. \nQue tal uma salada vegetariana refrescante?")
#     case _:
#         print("Vamos tentar de novo?")
        
print ("Digite um numero")      
num = int(input())

print ("O que gostaria de fazer?")
print ("\n[1]Adicionar item \n[2]Remover item \n[3]Listar Item \n[4]Sair\n")
opcao = int(input('Resposta: '))
match opcao:
    case 1 :
        num += 1
        print(f"Item adicionado. Agora temos o valor {num}")
    case 2:
        num -= 1
        print(f"Item removido. Agora temos o valor {num}")
    case 3:
        print(f"Listar Item {num}")
    case 4:
        print("Sair")
    case _:
        print("Vamos tentar de novo?")

        
