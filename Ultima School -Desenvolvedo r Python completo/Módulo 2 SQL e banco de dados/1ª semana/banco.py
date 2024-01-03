import sqlite3
conexao = sqlite3.connect('restricoes.sqlite3')
cursor = conexao.cursor()

sql = '''
create table cliente(id int, nome varchar(100), cpd varchar(11)unique)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()