# Crie um programa que receba um número inteiro e positivo e impreme seu fatorial.

nome = input("Olá usuário, digite seu nome: ")
print("Obrigado", nome)

numero = int(input("Preciso que você digite um numero inteiro e positivo: "))

if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item

print(fatorial)
