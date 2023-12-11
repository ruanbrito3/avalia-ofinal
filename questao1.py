salario = float(input("digite o seu salário cidadão de bem : "))

imposto1 = salario/100*8
imposto2 = salario/100*18
imposto3 = salario/100*28


if salario < 2000.01:
    print("fique feliz, você não pagará imposto")

elif salario < 3000.01:
    print(f"seu imposto é de :{imposto1} reais")

elif salario <= 4500.00:
    print(f"seu imposto é de :{imposto2} reais")

else:
    print(f"seu imposto é de :{imposto3} reais")






