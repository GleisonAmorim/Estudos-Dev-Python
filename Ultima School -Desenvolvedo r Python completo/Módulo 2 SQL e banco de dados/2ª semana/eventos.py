import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('Eventos.db') # <<< Definir nome do bd

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Executar um comando SQL para criar uma tabela
cursor.execute('''
CREATE TABLE Eventos (
    EventoID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Data TEXT NOT NULL,
    Local TEXT NOT NULL,
    OrganizadorID INTEGER,
    FOREIGN KEY (OrganizadorID) REFERENCES Organizadores(OrganizadorID)
);
''')

# Commitar as alterações e fechar a conexão
conn.commit()
conn.close()