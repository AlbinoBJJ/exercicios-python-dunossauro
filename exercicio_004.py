# Exercício 04
# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

# -------- minha solução --------

# l = input('Digite uma letra: ')

# if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u':
#     letra = 'CONSOANTE'
# else:
#     letra = 'VOGAL'
# print(f'A letra é uma {letra}')

# -------- solução da IA --------

while True:
    # 1. ENTRADA (Tratada)
    entrada = input('Digite uma letra: ').strip() # Não usamos .lower() aqui ainda
    
    # Verificamos se o usuário digitou algo vazio ou mais de uma letra
    if len(entrada) != 1:
        print('Erro: Digite apenas UM caracter.')
        continue # Pula para o início do loop

    # 2. VALIDAÇÃO (É letra?)
    if entrada.isalpha():
        # Agora sabemos que é letra. Vamos padronizar para minúscula
        letra = entrada.lower()
        
        if letra in 'aeiou':
            tipo = 'VOGAL'
        else:
            # Se é letra E não é vogal, só pode ser consoante
            tipo = 'CONSOANTE'
            
        # Saímos do loop pois deu tudo certo
        break
    
    else:
        # Se não for letra (número ou símbolo)
        print('Erro: O caracter digitado não é uma letra.')

# 3. SAÍDA
print(f'A letra é uma {tipo}')
