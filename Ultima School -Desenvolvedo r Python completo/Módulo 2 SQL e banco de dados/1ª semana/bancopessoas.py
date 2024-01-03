import sqlite3
conexao = sqlite3.connect('Brasil.sqlite3')
cursor = conexao.cursor()

sql = '''

)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()