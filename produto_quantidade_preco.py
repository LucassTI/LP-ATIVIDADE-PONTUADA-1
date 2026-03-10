import os

os.system("cls || clear")

print("Tabela de produtos: ")
print("""
    | Produto   | Até 9 unidades      | 10 unidades ou mais |
    | --------- | ------------------- | ------------------- |
    | Lápis     | R$ 1,00 por unidade | R$ 0,90 por unidade |
    | Borracha  | R$ 0,80 por unidade | R$ 0,70 por unidade |
    | Caneta    | R$ 1,20 por unidade | R$ 1,00 por unidade |
""")
# Entrada de dados
produto = input("Digite o nome do produto (lapis, borracha, caneta, corretivo): ").lower()
quantidade = int(input("Digite a quantidade adquirida: "))

# Definir preço unitário conforme produto e quantidade
if produto == "lapis":
    if quantidade < 10:
        preco_unitario = 1.00
    else:
        preco_unitario = 0.90

elif produto == "borracha":
    if quantidade < 10:
        preco_unitario = 0.80
    else:
        preco_unitario = 0.70

elif produto == "caneta":
    if quantidade < 10:
        preco_unitario = 1.20
    else:
        preco_unitario = 1.00

elif produto == "corretivo":
    if quantidade < 10:
        preco_unitario = 2.00
    else:
        preco_unitario = 1.50

else:
    print("Produto inválido!")
    preco_unitario = 0

# Cálculo do total
total = quantidade * preco_unitario

# Cálculo do desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Total a pagar
total_pagar = total - desconto

# Saída
print("\nProduto:", produto)
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total da compra: R$ {round(total, 2):.2f}")
print(f"Desconto: R$ {round(desconto, 2):.2f}")
print(f"Total a pagar: R$ {round(total_pagar, 2):.2f}")