import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
sql = '''
insert into categoria (descricao) values('celulares')
'''
cursor.execute(sql)
conexao.commit()
conexao.close()