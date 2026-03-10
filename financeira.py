import os
os.system("cls || clear")

renda = float(input("Digite o valor da renda: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
parcela = float(input("Digite o número de parcelas: "))

limite_emprestimo = renda * 10
prestacao = emprestimo / parcela
limite_prestacao = renda * 0.30
if emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("\nEmpréstimo aprovado!")
    print(f"Valor da prestação: R${prestacao:.2f}")
else:
    print("\nEmpréstimo não aprovado.")
