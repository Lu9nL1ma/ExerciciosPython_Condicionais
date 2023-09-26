# Exercício Python 07: Escreva um programa que pergunte o salário de um funcionário,
# E calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário atual: '))

if salario > 1250:
    novo_salario = salario + (salario * 10 / 100 )
    print('O seu salário de R$ {:.2f} com aumento de 10 por cento é de R$ {:.2f}'.format(salario, novo_salario))

else:
    novo_salario = salario + (salario * 15 / 100)
    print('O seu salário de R$ {:.2f} teve aumento de 15 por cento e está em R$ {:.2f}'.format(salario, novo_salario))
    