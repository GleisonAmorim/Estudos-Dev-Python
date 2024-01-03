import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('tarefas.db') # <<< Definir nome do bd

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Executar um comando SQL para criar uma tabela
cursor.execute('''CREATE TABLE Tarefas (
    TarefaID INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeTarefa TEXT NOT NULL,
    DataTarefa DATE NOT NULL,
    Concluida BOOLEAN NOT NULL DEFAULT 0,
    CategoriaID INTEGER,
    FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);
''')

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()