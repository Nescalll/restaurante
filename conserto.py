import sqlite3
import movimento as movimento

conn = sqlite3.connect('restaurante.db')
cursor = conn.cursor()

#cursor.execute('UPDATE funcionario SET senha = 200817 WHERE nome = "FAGNER"')
#conn.commit()


cursor.execute('SELECT * FROM funcionario WHERE nome = "SAMUEL"')
r =cursor.fetchall()
print(r)
#s = "200817"
#if(s in r[0]):
#    print(True)
#print(movimento.validarImportncia("200817"))