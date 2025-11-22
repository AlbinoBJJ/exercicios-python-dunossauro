# Exercício 03
# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

# F - Feminino
# M - Masculino
# Sexo Inválido.

# -------- minha solução --------

while True:

    l = input('Digite o sexo (F para FEMININO ou M para MASCULINO): ')

    if l == 'f' or l == 'F':
        escolha = 'FEMININO'
        break
    elif l == 'm' or l == 'M':
        escolha = 'MASCULINO'
        break
    else:
        print('Sexo INVÁLIDO. Digite o sexo (F para FEMININO ou M para MASCULINO): ')

print(f'O sexo é: {escolha}')

# -------- solução da IA --------

# # 1. ENTRADA JÁ TRATADA
# # .upper() -> Transforma 'f' em 'F'
# # .strip() -> Remove espaços acidentais (ex: ' F ')
# # [0] -> Pega só a primeira letra (caso digitem "Feminino")
# sexo = input('Digite o sexo (F/M): ').upper().strip()[0]

# # 2. LÓGICA LIMPA
# # Como já convertemos tudo para maiúsculo lá em cima,
# # só precisamos testar o 'F' e o 'M'.
# if sexo == 'F':
#     resultado = 'FEMININO'
# elif sexo == 'M':
#     resultado = 'MASCULINO'
# else:
#     resultado = 'SEXO INVÁLIDO'

# # 3. SAÍDA
# print(f'O sexo é: {resultado}')
