import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('Organizadores.db') # <<< Definir nome do bd

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Executar um comando SQL para criar uma tabela
cursor.execute('''
CREATE TABLE Organizadores (
    OrganizadorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    CPF TEXT NOT NULL UNIQUE
);
''')

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()