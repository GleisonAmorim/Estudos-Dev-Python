def test_calcular_total_pedido():
    assert calcular_total_pedido(100) == 9.0
    assert calcular_total_pedido(101) == 11.0
    assert calcular_total_pedido(105) == 17.0
    assert calcular_total_pedido(200) == 5.0
    assert calcular_total_pedido(201) == 4.0
    assert calcular_total_pedido(104) == 14.0
    assert calcular_total_pedido(202) == 0.0