try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # 'Exception as erro' coloca o erro dentro de uma variavel chamada erro, permitindo que o erro seja mostrado ao rodar o programa.
    print(f'O problema encontrado foi {erro.__class__}') # Mostra a classe do erro.
else: # Caso tenha dado certo (else é uma clausula opcional)
    print(f'O resultado é {r:.1f}')
finally: #  Executa independentemente de ter dado certo ou errado (também é uma cláusula opcional)
    print('Volte sempre! Muito obrigado!')