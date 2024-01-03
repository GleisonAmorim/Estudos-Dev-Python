import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('categorias.db') # <<< Definir nome do bd

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Executar um comando SQL para criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS Categorias (
    CategoriaID INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeCategoria TEXT NOT NULL
);
''')

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()