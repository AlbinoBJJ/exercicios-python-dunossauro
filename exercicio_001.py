# Exercício 01
# Faça um programa que peça dois números e imprima o maior deles.

# -------- minha solução --------

# 1. ENTRADA DE DADOS
# A função input() lê o que o usuário digita como texto (string).
# A função float() converte esse texto para número decimal, permitindo contas.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

# 2. PROCESSAMENTO (ESTRUTURA DE DECISÃO)
# Primeiro, verificamos o caso de igualdade.
# É uma boa prática verificar casos específicos ("edge cases") antes.
if n1 == n2:
    print('Números iguais')

# Se não forem iguais, o Python pula para cá (elif = else if).
# Verificamos se o primeiro é o vencedor.
elif n1 > n2:
    print('O primeiro número é maior')

# 3. SAÍDA FINAL (O DESCARTE)
# Se não são iguais e n1 não é maior, a única lógica possível é n2 ser maior.
# Por isso, não precisamos de outra condição (elif), basta o else.
else:
    print('O segundo número é maior')

# -------- solução da IA --------

# n1 = float(input('Digite o primeiro número: '))
# n2 = float(input('Digite o segundo número: '))

# # Aqui está a mágica:
# print("O maior número é:", max(n1, n2))
