try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else: # Caso tenha dado certo (else é uma clausula opcional)
    print(f'O resultado é {r:.1f}')
finally: #  Executa independentemente de ter dado certo ou errado (também é uma cláusula opcional)
    print('Volte sempre! Muito obrigado!')