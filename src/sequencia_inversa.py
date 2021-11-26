if __name__ == '__main__':
    sequencia = []
    n = 1
    tam = 1
    
    while n != 0:
        n = int(input("Digite um número: "))
        if n != 0:
            sequencia.append(n)
        else:
            tam = (len(sequencia)) - 1
            while tam >= 0:
                print(sequencia[tam])
                tam = tam - 1
