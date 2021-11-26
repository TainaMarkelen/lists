# Quebrar o problema em problemas menores

# Imprimir temperatura mínima e máxima

def MinMax():
    print ("A menor temperatura do mês foi {}°C.".format(minima(temps)))
    print ("A maior temperatura do mês foi {}°C.".format(maxima(temps)))
    
def minima(temps):
    menor = sys. maxsize
    for i in temps:
        if i < menor:
            menor = i
    return menor
    
def maxima(temps):
    maior = -sys.maxsize - 1
    for i in temps:
        if i > maior:
            maior = i
    return maior

if __name__ == '__main__':
    import sys
    temps = [0, 23, 38, 2, -3, 10, 18]
    MinMax()