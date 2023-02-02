salario_atual = float(input('Digite o salário: '))
salario_aumento = salario_atual + salario_atual * 10/100 if salario_atual > 1250.00 else \
                  salario_atual + salario_atual * 15/100

print(f'Seu salário era {salario_atual:.2f} e foi aumentado para {salario_aumento:.2f}')

#OU
if salario_atual > 1250:
    novo_salario = salario_atual + salario_atual * 0.10
    print(f'Seu salário era {salario_atual:.2f} e foi aumentado para {novo_salario:.2f}')
else:
    novo_salario = salario_atual + salario_atual * 0.15
    print(f'Seu salário era {salario_atual:.2f} e foi aumentado para {novo_salario:.2f}')

    
