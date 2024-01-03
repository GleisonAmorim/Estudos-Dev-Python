import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql = '''CREATE TABLE cliente (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	NOME TEXT(50),
	CPF TEXT(11),
	DATA_CADASTRO TEXT(10),
	ENDERECO TEXT(100)
);
'''
cursor.execute(sql)
conexao.commit()
conexao.close()