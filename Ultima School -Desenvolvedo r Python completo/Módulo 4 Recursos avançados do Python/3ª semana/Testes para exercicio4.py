def test_gerar_codigo():
    assert gerar_codigo() == 1
    assert gerar_codigo() == 2
    assert gerar_codigo() == 3

def test_cadastrar_peca():
    cadastrar_peca()
    assert len(pecas) == 1
    cadastrar_peca()
    assert len(pecas) == 2

def test_consultar_pecas():
    assert consultar_pecas(1) == [pecas[0]]
    assert consultar_pecas(2) == [pecas[1]]

def test_remover_peca():
    peca_remover = pecas[0]
    remover_peca(peca_remover['codigo'])
    assert len(pecas) == 1
    assert peca_remover not in pecas