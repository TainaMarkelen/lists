def soma_elementos(lista):
    soma = 0
    
    for i in lista:
        soma += i
        
    return (soma)


if __name__ == '__main__':
    lista = [4, 6, 5, 10]
    print (soma_elementos(lista))