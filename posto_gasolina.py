import os

os.system("cls || clear")

print("Tabela de Combustíveis: ")
print("""
    | Combustível | Preço por Litro  |
    | ----------- | ---------------- |
    | Gasolina    | R$ 6,59          |
    | Álcool      | R$ 3,79          |
""")
# Entrada de dados
litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")

# Preços base
preco_gasolina = 6.59
preco_alcool = 3.79

valor_total = 0

# Lógica para Álcool
if tipo_combustivel.lower() == 'álcool':
    if litros <= 25:
        # Desconto de 2%
        valor_total = litros * (preco_alcool * 0.98)
    else:
        # Desconto de 4%
        valor_total = litros * (preco_alcool * 0.96)

# Lógica para Gasolina
elif tipo_combustivel.lower() == 'gasolina':
    if litros <= 25:
        # Desconto de 3%
        valor_total = litros * (preco_gasolina * 0.97)
    else:
        # Desconto de 5%
        valor_total = litros * (preco_gasolina * 0.95)

else:
    print("Tipo de combustível inválido!")

# Saída do resultado
if valor_total > 0:
    print(f"O valor total a ser pago é: R$ {valor_total:.2f}")