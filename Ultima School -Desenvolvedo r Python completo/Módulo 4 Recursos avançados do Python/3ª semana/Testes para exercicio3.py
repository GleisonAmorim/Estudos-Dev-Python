def test_ler_dimensoes_objeto():
    assert ler_dimensoes_objeto(10, 20, 30) == 6000
    assert ler_dimensoes_objeto(5, 5, 5) == 125
    assert ler_dimensoes_objeto(0, 10, 20) == 0
    assert ler_dimensoes_objeto(-1, 15, 25) == 0

def test_calcular_preco_volume():
    assert calcular_preco_volume(500) == 10.0
    assert calcular_preco_volume(5000) == 20.0
    assert calcular_preco_volume(15000) == 30.0
    assert calcular_preco_volume(50000) == 20.0

def test_validar_medida():
    assert validar_medida("10") == 10
    assert validar_medida("abc") == -1
    assert validar_medida("-5") == -1
    assert validar_medida("20.5") == -1