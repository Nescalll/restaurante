import sqlite3
import movimento

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

key = False
while (key == False):
    nome = input('informe o nome do usuário:')
    senha = int(input('informe a senha do usuário:'))
#confirmar se o usuário e a senha existe
    key = movimento.validarEntrada(nome, senha)
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
                    movimento.visualizarTabela("funcionario", ["funcionario", "salario", "função", "senha"])
                case 2:
                    print('apenas funcionarios especificos podem acessar essa área. Para isso é necessario uma senha especial.')
                    verificacao = int(input('digite a senha:'))
                    cursor.execute('SELECT senha FROM funcionario WHERE funcao = "CHEFE"')
                    senha = cursor.fetchall()
                    match verificacao == senha:
                        case False:
                            print('senha incorreta')
                    match senha:
                        case True:
                            print("informe o funcionario, e a nova renda e sua nova função separados por um espaço.")
                            print("caso não queira mudar nada, basta repetir a função/renda")
                            [funcionario, renda, funcao] = input().split()
                            funcionarioExitente = True
                            cursor.execute('SELECT * FROM funcionario')
                            dados = cursor.fetchall()
                            for i in dados:
                                if(funcionario in i):
                                    funcionarioExitente = True
                case 3:
                    print('apenas funcionarios especificos podem acessar essa área. Para isso é necessario uma senha especial.')
                    verificacao = int(input('digite a senha:'))
                    cursor.execute('SELECT senha FROM funcionario WHERE funcao = "CHEFE"')
                    senha = cursor.fetchall()
                    match verificacao == senha:
                        case False:
                            print('senha incorreta')
                    match senha:
                        case True:
                            pass                    
                case _:
                    print("Ação invalida")

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