import os

os.system("cls || clear")

# SOLICITANDO DADOS

numero1 = float(input("Digite o valor do primeiro número: "))
numero2 = float(input("Digite o valor do segundo número: "))
soma_ab = numero1 + numero2

# condicional
if numero1 == numero2:
    print(f"Os números {numero1} e {numero2} são iguais, com essa condição o sistema irá somar eles.")
    soma = numero1 + numero2
    resultado = f"\nA soma dos números {numero1} e {numero2} é igual a {soma}."
    resultadofinal = f"Resultado: {soma}"
else:
    print(f"Os números {numero1} e {numero2} são diferentes, com essa condição o sistema irá multiplicar eles.")
    multiplicar = numero1 * numero2
    resultado = f"A multiplicação dos números {numero1} e {numero2} é igual a {multiplicar}."
    resultadofinal = f"Resultado: {multiplicar}"

# RESULTADO
print ("- Exibindo resultado -")
print(resultado)
print(f"\n{resultadofinal}")
