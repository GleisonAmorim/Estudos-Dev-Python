import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
sql ='''
CREATE TABLE contato_alternativo (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50),
	telefone TEXT(11)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()