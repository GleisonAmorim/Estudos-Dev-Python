import sqlite3
conexao = sqlite3.connect('Brasil.sqlite3')
cursor = conexao.cursor()

sql = '''
SELECT primeiro_nome, ultimo_nome FROM pessoas_santacatarina WHERE cor_cabelo = "branco";
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()