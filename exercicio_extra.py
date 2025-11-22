'''3. Exercício EXTRA: O Poder das Listas 📜 (proposto pelo GEMINI)
Até agora usamos o in em strings (textos). Mas o in brilha mesmo é com Listas.
Em uma string, 'banana' in 'bananada' funciona. 
Mas e se você quiser validar cupons de desconto exatos? 'ANA' estaria dentro de 'BANANA', o que seria um erro.
Com listas, a comparação é exata.

Desafio: Faça um sistema de validação de preços para um mercado. O programa deve pedir o nome de uma fruta para o caixa digitar.

Você tem uma lista de frutas em promoção: promo = ['banana', 'laranja', 'maça'].

Se a fruta digitada estiver na lista promo: O preço é R$ 2.00.

Se a fruta não estiver na lista, mas estiver no "sistema" (considere qualquer outra string não vazia): O preço é R$ 5.00.

(Opcional/Desafio) Tente fazer o while para não aceitar números ou entrada vazia.

Dica: A sintaxe para lista é com colchetes: lista = ['item1', 'item2']. O in funciona igualzinho!'''

# 1. CONFIGURAÇÃO INICIAL (BANCO DE DADOS)
# Criamos as listas fora do loop. Isso é ótimo para performance,
# pois o Python só precisa memorizar isso uma vez.
promo = ['banana', 'laranja', 'maça']
sistema = ['manga', 'kiwi', 'uva', 'limão', 'pera', 'mamão']

# 2. INÍCIO DO CICLO (LOOP)
# while True cria um loop infinito. O programa ficará preso aqui dentro
# até encontrar um comando 'break'.
while True:

    # 3. ENTRADA E LIMPEZA DE DADOS
    # input(): Espera o usuário digitar.
    # .lower(): Transforma tudo em minúsculo (ex: 'BaNaNa' vira 'banana').
    # .strip(): Remove espaços vazios antes e depois (ex: ' banana ' vira 'banana').
    fruta = input('Digite uma fruta da lista: ').lower().strip()
    
    # 4. VERIFICAÇÃO NA LISTA DE PROMOÇÃO
    # O operador 'in' verifica se a string 'fruta' existe dentro da lista 'promo'.
    if fruta in promo:
        valor = 2.00  # Define o preço
        break         # Encontrou? Ótimo! PARE o loop e pule para fora do while.

    # 5. VERIFICAÇÃO NO RESTO DO SISTEMA
    # Se não estava na promo, o código cai aqui. Verifica na segunda lista.
    elif fruta in sistema:
        valor = 5.00  # Define o outro preço
        break         # Encontrou? Ótimo! PARE o loop.

    # 6. TRATAMENTO DE ERRO
    # Se não estava em nenhuma das listas acima, cai aqui.
    else:
        print('Fruta não encontrada') 
        # Como NÃO tem 'break' aqui, o Python chega ao fim do bloco while
        # e volta automaticamente para a linha do 'input' lá em cima.

# 7. SAÍDA FINAL
# Essa linha só é executada depois que algum 'break' é acionado.
# O f-string usa :.2f para formatar o float com 2 casas decimais (ex: 2.00).
print(f'O preço da {fruta} é R$ {valor:.2f}')

# -------- solução da IA --------

# while True:
#     promo = ['banana', 'laranja', 'maça']
#     sistema = ['manga', 'kiwi', 'uva', 'limão', 'pera', 'mamão']

#     # .strip() é importante para remover espaços acidentais que o usuário digita
#     entrada = input('Digite uma fruta da lista: ').strip().lower()
    
#     # 1. VALIDAÇÃO DE VAZIO
#     # Se a string for vazia (""), ela conta como Falso no Python.
#     # "if not entrada" significa: "Se a entrada estiver vazia..."
#     if not entrada: 
#         print('Erro: Você não digitou nada!')
#         continue # Reinicia o loop imediatamente

#     # 2. VALIDAÇÃO DE NÚMEROS
#     # Testamos a variável 'entrada', pois 'fruta' ainda não existe oficialmente
#     if not entrada.isalpha():
#         print('Erro: Digite apenas letras (sem números ou símbolos).')
#         continue # Reinicia o loop

#     # 3. VERIFICAÇÃO DAS LISTAS (Agora sabemos que é um texto válido)
#     if entrada in promo:
#         valor = 2.00
#         fruta = entrada # Salvamos o nome certinho para usar no print final
#         break # Sai do loop (Vitória!)
        
#     elif entrada in sistema:
#         valor = 5.00
#         fruta = entrada
#         break # Sai do loop (Vitória!)
        
#     else:
#         # Se chegou aqui, é uma palavra, mas não temos no mercado
#         print('Não temos essa fruta no estoque. Tente outra.')

# # Fora do While
# print(f'O preço da {fruta} é R$ {valor:.2f}')