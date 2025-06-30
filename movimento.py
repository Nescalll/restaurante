import sqlite3
conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

def visualizarTabela(nomeDaTabela, colunas = []):
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
def validarEntrada(nome, senha):
    cursor.execute('SELECT * FROM funcionario')
    dados = cursor.fetchall()
    for info in dados:
        nomeConfirmado = str.lower(info[0]) == str.lower(nome)
        senhaConfirmado = int(info[3]) == senha
        if (nomeConfirmado and senhaConfirmado):
            return True
    return False
def validarExistencia(tabela, coluna, valor):
    pass
def alterarDado(tabela, valores):
    pass