def remove_repetidos(lista):
    lista.sort()
    final = len(lista) - 1
    proximo = 1
    
    for i in lista[:final]:
        if i == lista[proximo]:
            del lista[proximo - 1]
            final = final - 1
        else:
            proximo += 1
        
    print (lista)
        
    


if __name__ == '__main__':
    lista = [3, 4, 6, 3, 2, 1, 1, 1, 1, 5, 6, 6, 7]
    remove_repetidos(lista)
    