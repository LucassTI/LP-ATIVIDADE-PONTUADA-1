import os

os.system("cls || clear")

# SOLICITANDO DADOS

valor_a = float(input("Digite o valor de A: "))
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))
soma_ab = valor_a + valor_b


# VERIFICANDO O MAIOR NÚMERO
if soma_ab > valor_c:
    resultado = f"A soma de A + B ({soma_ab}) é maior que C ({valor_c})."
else:
    resultado = f"A soma de A + B ({soma_ab}) não é maior que C ({valor_c})."

# RESULTADO
print(f"\n -Exibindo resultado -")
print(resultado)