salario = float(input("digite seu salario meu funcionário : "))


aumento1 = salario/100*15
aumento2 = salario/100*12
aumento3 = salario/100*10
aumento4 = salario/100*7
aumento5 = salario/100*4



if salario <= 400.00:
    novosalario = salario + aumento1
    print(f"novo salario: {novosalario}")
    print(f"reajuste ganho: {aumento1}")
    print("em percentual: 15%")

elif salario <= 800.00:
    novosalario = salario + aumento2
    print(f"novo salario: {novosalario}")
    print(f"reajuste ganho: {aumento2}")
    print("em percentual: 12%")

elif salario <= 1200.00:
    novosalario = salario + aumento3
    print(f"novo salario: {novosalario}")
    print(f"reajuste ganho: {aumento3}")
    print("em percentual: 10%")

elif salario <= 2000.00:
    novosalario = salario + aumento4
    print(f"novo salario: {novosalario}")
    print(f"reajuste ganho: {aumento4}")
    print("em percentual: 7%")

else:
    novosalario = salario + aumento5
    print(f"novo salario: {novosalario}")
    print(f"reajuste ganho: {aumento5}")
    print("em percentual: 4%")