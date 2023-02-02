termo_atual = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtd_termos = 10
contagem = 0


while contagem < qtd_termos:
    print(termo_atual, end=' → ' if contagem != qtd_termos-1 else '\n')
    termo_atual += razao
    contagem += 1
    if contagem == qtd_termos:
        mais_termos = int(input('Quer mostrar quantos termos a mais? '))
        if mais_termos != 0:
            qtd_termos += mais_termos
        else:
            print(f'Fim da execução com {contagem} termos.')

