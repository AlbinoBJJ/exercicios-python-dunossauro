# Exercício 09
# Faça um programa que leia três números e mostre-os em ordem decrescente:

n1 = float(input('Digite o primeiro número: ').strip())
n2 = float(input('Digite o segundo número: ').strip())
n3 = float(input('Digite o terceiro número: ').strip())

maior = n1
medio = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

medio = (n1 + n2 + n3) - maior - menor

print(f'O número maior é {maior}, o número do meio é {medio} e o número menor é {menor}')



''' Solução da IA

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# 1. Garante que o n1 é maior que o n2
if n1 < n2:
    n1, n2 = n2, n1

# 2. Garante que o n1 é maior que o n3
# (Agora o n1 é o campeão absoluto, o maior de todos)
if n1 < n3:
    n1, n3 = n3, n1

# 3. Resolve a briga pelo segundo lugar entre n2 e n3
if n2 < n3:
    n2, n3 = n3, n2

print(f'A ordem decrescente é: {n1}, {n2} e {n3}')'''

