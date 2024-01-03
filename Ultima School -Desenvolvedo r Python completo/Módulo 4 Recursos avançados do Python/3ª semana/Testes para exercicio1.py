def test_calcula_valor_com_desconto():
    assert calcular_valor_com_desconto(10.0, 5) == 50.0
    assert calcular_valor_com_desconto(8.0, 15) == 102.0
    assert calcular_valor_com_desconto(15.0, 8) == 120.0
    assert calcular_valor_com_desconto(20.0, 10) == 180.0
    assert calcular_valor_com_desconto(12.0, 20) == 216.0

def test_calcula_valor_sem_desconto():
    assert calcular_valor_sem_desconto(10.0, 5) == 50.0
    assert calcular_valor_sem_desconto(8.0, 15) == 120.0
    assert calcular_valor_sem_desconto(15.0, 8) == 120.0
    assert calcular_valor_sem_desconto(20.0, 10) == 200.0
    assert calcular_valor_sem_desconto(12.0, 20) == 240.0
