import sqlite3

conn = sqlite3.connect('m1s3.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedor (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        produto TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS endereco (
        id INTEGER PRIMARY KEY,
        fornecedor_id INTEGER,
        rua TEXT,
        numero TEXT,
        FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
    )
''')

cursor.execute("INSERT INTO fornecedor (id, nome) VALUES (3, 'Padaria do Pão')")
cursor.execute("INSERT INTO fornecedor (id, nome, produto) VALUES (4, 'Marcenaria Martelo', 'Carnes')")

cursor.execute("INSERT INTO endereco (id, fornecedor_id, rua, numero) VALUES (5, 3, 'Rua da Padaria, 123', '')")
cursor.execute("INSERT INTO endereco (id, fornecedor_id, rua, numero) VALUES (6, 4, 'Avenida da Marcenaria, 456', '')")

cursor.execute("UPDATE endereco SET rua = 'Rua dos Peixes', numero = '26' WHERE fornecedor_id = 2")

cursor.execute("SELECT * FROM fornecedor")
fornecedores = cursor.fetchall()
print("Todos os fornecedores:")
print(fornecedores)

cursor.execute("SELECT * FROM fornecedor WHERE produto = 'Carnes'")
fornecedores_carnes = cursor.fetchall()
print("\nFornecedores com produto igual a Carnes:")
print(fornecedores_carnes)

cursor.execute("DELETE FROM fornecedor WHERE id = 1")

conn.commit()
conn.close()
