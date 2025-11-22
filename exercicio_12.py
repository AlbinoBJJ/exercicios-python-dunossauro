'''Exercício 12
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR: 
- Salário Bruto até 900 (inclusive) - isento 
- Salário Bruto até 1500 (inclusive) - desconto de 5% 
- Salário Bruto até 2500 (inclusive) - desconto de 10% 
- Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00'''

print('\n')
valor_hora = float(input('Digite o valor do salário recebido por hora trabalhada: ').strip())
qtde_hora = float(input('Digite a quantidade de horas trabalhadas no mês: ').strip())

sal_bruto = valor_hora * qtde_hora

if sal_bruto <= 900:
    imposto = 0
elif 900 < sal_bruto <= 1500:
    imposto = 0.05
elif 1500 < sal_bruto <= 2500:
    imposto = 0.1
else:
    imposto = 0.2

desconto_ir = sal_bruto * imposto

if imposto == 0:
    ir_print = 'Isento'
else:
    ir_print = f'{int(imposto * 100)}%'

desconto_sindicato = sal_bruto * 0.03

desconto_inss = sal_bruto * 0.1

total_desc = desconto_ir + desconto_sindicato + desconto_inss

fgts = sal_bruto * 0.11

sal_liquido = sal_bruto - total_desc

text_desc_bruto = f'Salário Bruto: (R$ {valor_hora:.2f} * {qtde_hora}h)'
text_desc_ir = f'(-) IR ({ir_print})'
text_desc_sind = '(-) Sindicato (3%)'
text_desc_inss = '(-) INSS (10%)'
text_desc_fgts = 'FGTS (11%)'
text_desc_total_desc = 'Total de descontos'
text_desc_liquido = 'Salário Líquido'
text_sal_bruto = f'{sal_bruto:.2f}'
text_ir = f'{desconto_ir:.2f}'
text_sind = f'{desconto_sindicato:.2f}'
text_inss = f'{desconto_inss:.2f}'
text_fgts = f'{fgts:.2f}'
text_total_desc = f'{total_desc:.2f}'
text_sal_liquido = f'{sal_liquido:.2f}'

print(f'\n{text_desc_bruto:<40} : R$ {text_sal_bruto:>10}\n{text_desc_ir:<40} : R$ {text_ir:>10}\n{text_desc_sind:<40} : R$ {text_sind:>10}\n{text_desc_inss:<40} : R$ {text_inss:>10}\n{text_desc_fgts:<40} : R$ {text_fgts:>10}\n{text_desc_total_desc:<40} : R$ {text_total_desc:>10}\n{text_desc_liquido:<40} : R$ {text_sal_liquido:>10}\n')