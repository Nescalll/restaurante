import sqlite3

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

key = False
while (key == False):
    nome = input('informe o nome do usuário:')
    senha = int(input('informe a senha do usuário:'))
#confirmar se o usuário e a senha existe
    cursor.execute('SELECT * FROM funcionario')
    dados = cursor.fetchall()
    for info in dados:
        nomeConfirmado = str.lower(info[0]) == str.lower(nome)
        senhaConfirmado = info[3] == senha
        if (nomeConfirmado and senhaConfirmado):
            key = True
            break
    if(key == False):
        print('nome ou senha errado, comfirme se alguns deles esta errado e tente novamete')
while (key == True):
    inicio = int(input('[1]funcionarios \n[2] clientes \n[3] produto \n[4] sair \n: '))
    match inicio:
#categoria de funcionarios.
        case 1:
            funcionario = int(input('[1]ver funcionarios \n[2]alterar funcionario \n[3] adicionar/excluir funcionario \n:'))
            match funcionario:
                case 1:
                    cursor.execute('SELECT * FROM funcionario')
                    dados = cursor.fetchall()

                    for i in dados:
                        print('funcionario:', i[0],'renda:', i[1],'função:', i[2])
#categoria de clientes.
        case 2:
            cliente = int(input('[1] ver cliente \n[2]alterar cliente \n[3]adicionar/excluir cliente \n:'))
            match cliente:
                case 1:
                    cursor.execute('SELECT * FROM cliente')
                    dados = cursor.fetchall()

                    for i in dados:
                        print('cliente:',i[0],'nome:',i[1],'historico:')
#categoria de produtos.
        case 3:
            produtos= int(input('[1] ver produtos \n[2]alterar produtos \n[3]adicionar/exluir produtos \n:'))
            match produtos:
                case 1:
                    cursor.execute('SELECT * FROM produtos')
#sair do programa.
        case 4:
            key = False
        case _:
            print('não existe essa função.\n tente novamente!')