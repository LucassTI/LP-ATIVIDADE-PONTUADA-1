import os
os.system("cls || clear")


print ("- Recebendo dados -")
numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação desejada +,-,*,/ (soma, subtração, multiplicação ou divisão): ")

if operador == "+":
    resultado = numero1 + numero2
    operacao = "Soma"
elif operador == "-":
    resultado = numero1 - numero2
    operacao = "Subtração"
elif operador == "*":
    resultado = numero1 * numero2
    operacao = "Multiplicação"
elif operador == "/":
    resultado = numero1 / numero2
    operacao = "Divisão"
else:
   resultado = "Operador inválido."
   
# Exibindo resultados
print(f"\n- Exibindo resultado -")

print(f"Numero 1: {numero1}")
print(f"Numero 2: {numero2}")
print(f"Operação desejada: {operacao}")
print(f"Resultado: {resultado}")
