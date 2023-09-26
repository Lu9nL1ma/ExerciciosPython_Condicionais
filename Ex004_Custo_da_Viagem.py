# Exercício Python 04: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# E R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem (Km): '))

if distancia <= 200:
    preco = distancia * 0.5
    print('O preço da passagem para essa distância é R$ {:.2f}.'.format(preco))

else: 
    preco = distancia * 0.45
    print('Para essa distância o preço da passagem é de R$ {:.2f}'.format(preco))
