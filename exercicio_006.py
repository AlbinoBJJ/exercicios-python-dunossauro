# Exercício 06
# Faça um programa que leia três números e mostre o maior deles:

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# 1. Assumimos que o n1 é o dono do pedaço
maior = n1
valor = 'primeiro'

# 2. Desafiamos o 'maior'
if n2 > maior:
    maior = n2
    valor = 'segundo'
if n3 > maior:
    maior = n3
    valor = 'terceiro'

print(f'O {valor} é o maior número e seu valor é {maior}')
