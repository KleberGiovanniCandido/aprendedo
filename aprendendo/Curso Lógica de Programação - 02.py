# Crie um programa que recebe dois valores e exibe qual é o maior entre eles

nome = input("Olá usuário, por favor digite seu nome: ")

print("Muito bem ", nome)
numero1 = input("Por favor, digite um número:")

print("Agora", nome)
numero2 = input("Digite outro número:")

if int(numero1) > int(numero2):
    print("O número", numero1, "é o maior entre eles")
else:
    print("O número", numero2, "é o maior entre eles")

