# Exercício Python 08: Desenvolva um programa que leia o comprimento de três retas
# E diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Analisando Triangulos')
print('-=-' * 20)

reta_1 = float(input('Insira o comprimento do primeiro segmento: '))
reta_2 = float(input('Insira o comprimento do segundo segmento: '))
reta_3 = float(input('Insira o comprimento do terceiro segmento: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2: 
    print('Os segmentos podem formar um triângulo!')

else:
    print('Os segmentos NÂO podem formar um triângulo!')
