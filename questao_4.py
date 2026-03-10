import os

os.system("cls || clear")

print("Tabela de Frutas: ")
print("""
    | Produto | Até 5 Kg       | Acima de 5 Kg  |
    | Morango | R$ 2,50 por Kg | R$ 2,20 por Kg |
    | Maçã    | R$ 1,80 por Kg | R$ 1,50 por Kg |
""")
fruta = input("Digite o nome da fruta desejada: ")
peso = float(input("Digite o peso da fruta (em Kg): "))

if fruta.lower() == "morango":
    if peso <= 5:
        preco = 2.50 * peso
        desconto = print("Não há desconto.")
    
    
    else:
        preco = 2.20 * peso
        peso <= 10 or preco > 15
        desconto = preco * 0.10
        valor_final = preco - desconto


elif fruta.lower() == "maçã" or fruta.lower() == "maca":
    if peso <= 5:
        preco = 1.80 * peso
        desconto = print("Não há desconto.")
    
    
    else:
        preco = 1.50 * peso
        peso <= 10 or preco > 15
        desconto = preco * 0.10
        valor_final = preco - desconto
else:
    print("Fruta não disponível.")
    preco = 0

if preco > 0:
    print(f"O preço total para {peso} Kg de {fruta} é R$ {valor_final:.2f}.")
    print(f"O desconto aplicado é R$ {desconto:.2f}.")
