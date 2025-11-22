# Exercício 02
# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# -------- minha solução --------

# 1. ENTRADA DE DADOS
# O uso de float() é perfeito aqui, pois o usuário pode digitar 
# números decimais (como -1.5 ou 0.001).
num = float(input('Digite um número: '))

# 2. TRATAMENTO DE CASO ESPECÍFICO (Zero)
# Começar verificando o zero é uma ótima estratégia para eliminar 
# o caso "neutro" logo de cara.
if num == 0:
    print('O número é ZERO')

# 3. VERIFICAÇÃO DE POSITIVO
# Se não for zero, o código cai aqui. Verificamos se é maior que zero.
elif num > 0:
    print('O número é POSITIVO')

# 4. CONCLUSÃO (Negativo)
# Se falhou nas duas anteriores, matematicamente só resta ser negativo.
# O 'else' captura essa "sobra" lógica sem precisar testar (num < 0).
else:
    print('O número é NEGATIVO')

# -------- solução da IA --------

# num = float(input('Digite um número: '))

# # Definimos apenas uma variável com o "rótulo" do número
# if num == 0:
#     resultado = 'ZERO'
# elif num > 0:
#     resultado = 'POSITIVO'
# else:
#     resultado = 'NEGATIVO'

# # Imprimimos uma única vez usando f-string (o 'f' antes das aspas)
# # Isso permite colocar a variável direto no texto entre chaves {}
# print(f'O número é {resultado}')