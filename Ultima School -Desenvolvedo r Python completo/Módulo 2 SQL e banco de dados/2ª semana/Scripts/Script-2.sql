CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nota TEXT,
    produto TEXT,
    valor FLOAT NOT NULL,
    data_da_venda FLOAT,
    tipo_pagamento TEXT(255),
    defeito TEXT(255),
    outro1 TEXT(255),
    outro2 TEXT(255)
);