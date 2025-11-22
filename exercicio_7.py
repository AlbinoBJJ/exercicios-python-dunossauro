# Exercício 07
# Faça um programa que leia três números e mostre o maior e o menor deles:

# minha solução

# n1 = float(input('Digite o primeiro número: '))
# n2 = float(input('Digite o segundo número: '))
# n3 = float(input('Digite o terceiro número: '))

# if (n1 >= n2) and (n1 >= n3):
#     result_max = n1
# elif (n2 >= n1) and (n2 >= n3):
#     result_max = n2
# else:
#     result_max = n3

# if (n1 <= n2) and (n1 <= n3) :
#     result_min = n1
# elif (n2 <= n1) and (n2 <= n3):
#     result_min = n2
# else:
#     result_min = n3

# print (f'O número maior é {result_max} e o número menor é {result_min}')

# solução da IA

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# 1. Assumimos que o n1 é o dono do pedaço
maior = n1
menor = n1

# 2. Desafiamos o 'maior'
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# 3. Desafiamos o 'menor'
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O número maior é {maior} e o número menor é {menor}')