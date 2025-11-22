# Exercício 05
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# 1. LOOP INFINITO (O porteiro assume o posto)
while True:
    
    # Solicitamos os dados a cada nova tentativa
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    # 2. A BARREIRA DE SEGURANÇA (Validação)
    # O Python verifica: n1 está entre 0 e 10? E n2 também?
    if (0 <= n1 <= 10) and (0 <= n2 <= 10):
        
        # --- ÁREA VIP (Onde o cálculo acontece) ---
        # Só entramos aqui se as notas forem válidas.
        media = (n1 + n2) / 2

        if media == 10:
            resultado = 'APROVADO COM DISTINÇÃO'
        elif media >= 7:
            resultado = 'APROVADO'
        else:
            resultado = 'REPROVADO'
            
        print(f'Média: {media}. Situação: {resultado}')
        
        # 3. SAÍDA TRIUNFAL
        # Deu tudo certo, cálculo feito. Quebramos o loop e encerramos o programa.
        break

    else:
        # 4. O BARRADO
        # Se as notas não passaram no 'if' lá de cima, caem aqui.
        print('ERRO: Uma ou mais notas digitadas é inválida (deve ser de 0 a 10).')
        # Como NÃO tem break aqui, o Python bate no final do while
        # e volta automaticamente para a linha do 'input' lá em cima.
