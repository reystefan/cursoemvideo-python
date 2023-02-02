from lib import interface
from time import sleep
from lib.arquivo import *       # Nessa forma de importação, nao precisa referenciar o módulo do método utilizado

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opc = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opc == 3:
        interface.titulo('Saindo do sistema. . . Até logo!')
        break
    elif opc == 1:
        # Listar conteudo de um arquivo
        lerArquivo(arq)
    elif opc == 2:
        # Cadastrar uma nova pessoa
        interface.titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(2)
