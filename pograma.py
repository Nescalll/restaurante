import sqlite3
import movimento as movimento

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

key = False
while (key == False):
    nome = input('informe o nome do usuário:')
    senha = int(input('informe a senha do usuário:'))
#confirmar se o usuário e a senha existe
    key = movimento.validarEntradaDeFuncionario(nome, senha)
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
                    verificacao = input('digite a senha:')
                    match movimento.validarImportncia(verificacao):
                        case False:
                            print('senha incorreta')
                        case True:
                            print("informe o funcionario, e a nova renda e sua nova função separados por um espaço.")
                            print("caso não queira mudar nada, basta repetir a função/renda")
                            [funcionario, salario, funcao] = input().split()
                            funcionarioExitente = movimento.validarExistencia("funcionario", "nome", funcionario)
                            match funcionarioExitente:
                                case False:
                                    print("O funcionario não existe")
                                case True:
                                    movimento.alterarDado("funcionario", ["salario", "funcao"], [salario, funcao.upper()], "nome", funcionario.upper())
                                    print("usurio adicionado")
                case 3:
                    acaoDoUsuario = int(input("O que deseja? \n[1]criar \n[2]excluir \n"))
                    print('apenas funcionarios especificos podem acessar essa área. Para isso é necessario uma senha especial.')
                    verificacao = input('digite a senha:')
                    match movimento.validarImportncia(verificacao):
                        case False:
                            print('senha incorreta')
                        case True:
                            match acaoDoUsuario:
                                case 1:
                                    print("Para adicionar um novo funcionario")
                                    print("informe o nome, salario, funcao e senha do novo funcionario")
                                    [nome, salario, funcao, senha] = input(":").split()
                                    cursor.execute("INSERT INTO funcionario (nome, salario, funcao, senha) VALUES (?,?,?,?)", (nome, salario, funcao, senha))
                                    conn.commit()
                                case 2:
                                    nome = input("Digite o nome do usuario \n:")
                                    match movimento.validarExistencia(nome):
                                        case True:
                                            cursor.execute("DELETE FROM funcionario WHERE nome = '"+nome+"'")
                                            conn.commit()
                                            print("O funcionario foi excluido")
                                        case False:
                                            print("Funcionario não existe")
                case _:
                    print("Ação invalida")

#categoria de clientes.
        case 2:
            cliente = int(input('[1] ver cliente \n[2]alterar cliente \n[3]adicionar/excluir cliente \n:'))
            match cliente:
                case 1:
                    movimento.visualizarTabela("cliente", ["nome"])
                case _:
                    print("Ação invalida")

#categoria de produtos.
        case 3:
            produtos= int(input('[1] ver produtos \n[2]alterar produtos \n[3]adicionar/exluir produtos \n:'))
            match produtos:
                case 1:
                    movimento.visualizarTabela("produto", ["nome", "preco", "quantidade","validade"])
                case _:
                    print("Ação invalida")                    

#sair do programa.
        case 4:
            key = False
            conn.close()
        case _:
            print('não existe essa função.\n tente novamente!')