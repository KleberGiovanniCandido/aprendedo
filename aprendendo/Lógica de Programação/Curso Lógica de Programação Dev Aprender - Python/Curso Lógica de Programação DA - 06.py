# Escreva um programa que retorna o valor hora de um funcinário com base no seu salário mensal e
# horas trabalhadas por mês.

print("Olá usuário, qual é o seu nome?")
nome = input()

print("Muito bem", nome,"diga agora, qual é o seu salário? ")
salario = int(input())

print("Entendi", nome,"me fale quantas horas vc trabalha por dia? ")
horas = int(input())

print(nome, "quantos dias você trabalha por semana? ")
dias = int(input())

hora_semana = horas * dias
dias_mes = dias * 4
hora_mes = horas * dias_mes
valor_por_hora = (hora_semana / dias)



print(nome, "você trabalha", hora_semana, "horas por semana em um total de", hora_mes, "horas no mês, com", dias_mes, "dias trabalhados")
print("Seu sálario é de R$", salario, "e você está recebendo R$", valor_por_hora, "por hora trabalhada.")