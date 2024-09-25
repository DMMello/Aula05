import os
os.system("cls")
print(30*"=")
turno = int(input('Informe o número do turno (1,2 ou 3) :'))
match turno:
    case 1:
        print("Manha")
    case 2:
        print("Tarde")
    case 3:
        print("Noite")
    case _:
        print("Inválido")
