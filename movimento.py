import sqlite3
conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

def visualizarTabela(nomeDaTabela, colunas = []):
<<<<<<< HEAD
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
=======
>>>>>>> ddd2de81d92156b695cb68edf9010b8be9276602
    cursor.execute("SELECT * FROM "+nomeDaTabela)
    dados = cursor.fetchall()
    voltas = 0
    for i in dados:
        for j in colunas:
            print(j+":",str(i[voltas])+"; ", end="")
            voltas += 1
        voltas = 0
        print()
    return
<<<<<<< HEAD
def validarEntradaDeFuncionario(nome, senha):
=======
def validarEntrada(nome, senha):
>>>>>>> ddd2de81d92156b695cb68edf9010b8be9276602
    cursor.execute('SELECT * FROM funcionario')
    dados = cursor.fetchall()
    for info in dados:
        nomeConfirmado = str.lower(info[0]) == str.lower(nome)
        senhaConfirmado = int(info[3]) == senha
        if (nomeConfirmado and senhaConfirmado):
            return True
    return False
def validarExistencia(tabela, coluna, valor):
<<<<<<< HEAD
    cursor.execute("SELECT "+coluna+" FROM "+tabela)
    tabelaDeNomes = cursor.fetchall()
    for i in tabelaDeNomes:
        if(valor.upper() in i):
            return True
    return False
def alterarDado(tabela, coluna, valores, colunaChave, valorChave):
    for i in range(len(coluna)):
        cursor.execute("UPDATE "+tabela+" SET "+coluna[i]+" = '"+valores[i]+"' WHERE "+colunaChave+" = '"+valorChave+"'")
        conn.commit()
    return
def validarImportncia(senha):
    cursor.execute('SELECT senha FROM funcionario WHERE funcao = "CHEFE"')
    senhaReal = cursor.fetchall()
    if(senha in senhaReal[0]):
        return True
    return False
=======
    pass
def alterarDado(tabela, valores):
    pass
>>>>>>> ddd2de81d92156b695cb68edf9010b8be9276602
