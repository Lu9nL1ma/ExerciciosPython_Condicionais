# Exercício Python 03: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um numero: '))

if numero % 2 == 0:
    print('O número {} é par!'.format(numero))

else:
    print('O número {} é ímpar!'.format(numero))
    