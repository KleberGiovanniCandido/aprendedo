#Chute um número, escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um
#número até que o valor aleatório gerado no início do programa seja chutado corretamente. O programa deve informar caso
#o chute tenha sido acima, abaixo ou igual ao valor aleatório gerado no início do programa.

import random

numero_aleatorio = random.randint(1, 10)

acertou = False

while acertou == False:
    chute = int(input("Digite um número entre 1 e 10: "))
    if chute > numero_aleatorio:
        print("O número é menor")
    if chute < numero_aleatorio:
        print("O numero é maior")
    elif chute == numero_aleatorio:
        acertou = True
        print("Você acertou!!! Parábens!!")
