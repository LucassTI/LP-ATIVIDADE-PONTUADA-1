import os
os.system("cls || clear")

nome = input("Digite o seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    resultado = "Aprovado"
elif media >= 4:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"\n- Exibindo informações -")
print(f"Nome: {nome}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")
print(f"Resultado: {resultado}")