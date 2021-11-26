def maior_elemento(lista):
    maior = -sys.maxsize - 1
    
    for i in lista:
        if i > maior:
            maior = i
    
    return maior
    

if __name__ == '__main__':
    lista = [1, 5, 5, 8, 2, 3, 19, 9, 82, 0]
    import sys
    print (maior_elemento(lista))
    