def minima(temps):
    menor = sys. maxsize
    for i in temps:
        if i < menor:
            menor = i
    return menor

def teste_pontual(temps, valor_esperado):
    valor_calculado = minima(temps)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temps)
        print("Valor esperado: {}, valor calculado: {}".format(valor_esperado, valor_calculado))

def testa_minimo():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([-10, 0, 3], -10)
    teste_pontual([2, 1, 29, 35], 1)
    teste_pontual([-8, 27, 14, 40], -8)
    print("Finalizando os testes")

if __name__ == '__main__':
    import sys
    testa_minimo()