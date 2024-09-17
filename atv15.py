# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
n = float(input("1n"))
n1 = float(input("2n"))
op = input("soma subtração multiplicação divisão")

if op == "soma":
    print(n+n1)
elif op == "subtração":
    print(n-n1)
elif op == "divisão":
    print(n/n1)
