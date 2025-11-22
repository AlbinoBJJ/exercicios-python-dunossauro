'''Exercício 11
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:

- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.'''

salario = float(input('Digite seu salário: '))

if salario <= 280.0:
    percentual = 0.2
elif (salario > 280.0) and (salario <= 700.0):
    percentual = 0.15
elif (salario > 700.0) and (salario <= 1500.0):
    percentual = 0.1
else:
    percentual = 0.05

aumento = salario * percentual

novo_salario = salario + aumento

print(f'O seu salário atual é de: R$ {salario:.2f}\nO percentual de reajuste é de: {int(percentual*100)}%\nO aumento que você irá receber é de: R$ {aumento:.2f}\nO seu salário com reajuste será de: R$ {novo_salario:.2f}.')