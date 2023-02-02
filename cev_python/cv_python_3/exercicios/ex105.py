def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: Várias notas.
    :param sit: (opcional) Adiciona a situação do aluno de acordo com sua média de notas.
    :return: retorna um dicionário com as notas e a situação do aluno, caso seja requerida.
    '''
    soma = 0
    dados = {}
    dados['total'] = len(n)
    c = 0
    while c < len(n):
        if c == 0:
            maior = n[c]
            menor = n[c]
        elif n[c] > maior:
            maior = n[c]
        elif n[c] < menor:
            menor = n[c]
        soma += n[c]
        c += 1
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = soma / len(n)

    if sit:
        if 6 > dados['media'] >= 5:
            dados['situacao'] = 'RECUPERAÇÃO'
        elif dados['media'] < 5:
            dados['situacao'] = 'REPROVADO'
        else:
            dados['situacao'] = 'APROVADO'
    return dados.copy()

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)