# Exercício Python 02: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do veículo (Km/h)? '))
multado = (velocidade-80) * 7

if velocidade < 80:
    print('Parabéns! O veículo está abaixo do limite permitido de 80Km/h!')

else:
    print('Acima do limite de 80Km/h! Você foi multado em R$ {:.2f}!'.format(multado))
    