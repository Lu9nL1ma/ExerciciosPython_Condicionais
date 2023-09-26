# Exercício Python 06: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))
maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2

elif numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

print('O maior número é: {}'.format(maior))

menor = numero_1

if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2

elif numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

print('O menor número é: {}'.format(menor))
