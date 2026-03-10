import os

os.system("cls || clear")


cor_cd = input("Digite a cor do CD: ")

if cor_cd.lower() == "verde":
    print("\nO Cd custa R$10,00")
elif cor_cd.lower() == "vermelho":
    print("\nO Cd custa R$40,00")
elif cor_cd.lower() == "azul":
    print("\nO Cd custa R$20,00")
elif cor_cd.lower() == "amarelo":
    print("\nO Cd custa R$30,00")
else:
    print("\nCor do CD não reconhecida.")
