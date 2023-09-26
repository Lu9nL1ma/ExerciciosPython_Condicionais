# Exercício Python 01: Escreva um programa que faça o computador “pensar” em
# Um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# Qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero_pc = randint(0, 5)

print('-' * 58)
print('Estou pensando em um número de 0 a 5. Tente adivinhar...')
print('-' * 58)

numero_jogador = int(input('Em que número pensei? '))
print('Conferindo número...')
sleep(2)

if numero_jogador == numero_pc:
    print('Parabéns! Você ganhou!')
else: 
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(numero_pc, numero_jogador))
