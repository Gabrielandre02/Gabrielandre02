opção = int(input('insirir dados? 0 - Não       1 - Sim'))
while opção == 0:
    print('Encerrando o progama !')
    break
while opção == 1:
    print('Os Conceitos das notas sao  A, B, C, D, E')
    nome = input('Qual o nome do aluno:')
    nota = float(input('Qual a nota do aluno:'))
        
    if 0 <= nota < 3:
        conceito = 'E'
    elif 3 <= nota < 5:
        conceito = 'D'
    elif 5 <= nota < 7:
        conceito = 'C'
    elif 7 <= nota < 9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:
        print('Nota invalida, encerrando o progama.')
        exit()
    
    print('O aluno(a) {} tirou a nota {} e se encaixa no conceito {}'.format(nome, nota, conceito))
    opção = int(input('insirir dados? 0 - Não       1 - Sim'))
while opção == 0:
    print('Encerrando o progama !')
    break
