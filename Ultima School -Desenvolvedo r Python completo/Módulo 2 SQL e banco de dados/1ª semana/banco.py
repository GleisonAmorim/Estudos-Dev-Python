import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql = '''
create table categoria(
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao text(100)
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()