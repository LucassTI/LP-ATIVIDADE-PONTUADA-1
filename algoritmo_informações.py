import os

os.system("cls || clear")

# SOLICITANDO DADOS

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")


# VERIFICANDO O MAIOR NÚMERO
if sexo.lower() == "feminino" and estado_civil.lower() == "casada":
    tempo_casada = int (input("Qual o seu tempo de casada (em anos): "))
    print(f"{nome}, você é do sexo {sexo}, casada e tem {tempo_casada} anos de casada.")
else:
    print(f"{nome}, você é do sexo {sexo} e tem estado civil {estado_civil}.")
