def decorator_imprimir(func):
    def wrapper(capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print(f"Parâmetros: Capital={capital}, Taxa={taxa}, Tempo={tempo}")
        print(f"Resultado da função: {resultado}")
        return resultado
    return wrapper

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    return juros

# Testando a função decorada
juros_calculados = juros_simples(1000, 0.05, 2)
