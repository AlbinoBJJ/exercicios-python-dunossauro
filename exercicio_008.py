# Exercício 08
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

p1 = float(input('Digite o preço do primeiro produto: R$ ').strip())
p2 = float(input('Digite o preço do segundo produto: R$ ').strip())
p3 = float(input('Digite o preço do terceiro produto: R$ ').strip())

menor = p1
escolha = 'primeiro'

if p2 < menor:
    menor = p2
    escolha = 'segundo'
if p3 < menor:
    menor = p3
    escolha = 'terceiro'

print(f'O {escolha} produto tem o menor preço e seu valor é de: R$ {menor:.2f}')
