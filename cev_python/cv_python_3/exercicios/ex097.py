def escreva(txt):
    print('~'*(len(txt) + 8))
    print(f'{txt:^{len(txt) + 8}}')
    print('~'*(len(txt) + 8))

escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
