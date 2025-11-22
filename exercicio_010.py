''' Exercício 10
Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

periodos = ['Matutino (manhã)', 'Vespertino (tarde)', 'Noturno (noite)']
while True:

    for i, opt in enumerate(periodos):
        print(i+1, '. ', opt)

    entrada = int(input('Digite o período que você estuda (apenas o número): '))

    if entrada == 1:
        print('Bom dia!')
        break
    elif entrada == 2:
        print('Boa tarde!')
        break
    elif entrada == 3:
        print('Boa noite!')
        break
    else:
        print('Valor Inválido!')
