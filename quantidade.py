if __name__ == '__main__':
    #lista com todos os primos menores que 100
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print (primos)
    
    #tamanho/comprimento
    print (len(primos))
    
    #local
    filme = ["Como eu era antes de você", "Me", 1.23, 1995]
    print (filme[0])
    print (filme[-2])
    
    #tipo dos elementos da lista
    print (type(filme[0]))
    
    print (type(filme[2]))
    
    #acrescentando elementos no final da lista
    filme.append("mais um")
    
    print(filme)
    
    #listas vazias
    cartoes_amarelos = []
    cartoes_amarelos.append("Luiz")
    cartoes_amarelos.append(1)
    print (cartoes_amarelos)
    
    cartoes_amarelos.append("Neymar")
    cartoes_amarelos.append(78)
    print (cartoes_amarelos)
    
    #substituir um valor
    cartoes_amarelos[3] = 20
    #78 receberá 20 no lugar
    print (cartoes_amarelos)
    
    #atribuir um valor
    s = []
    s.append(100)
    s[0] = s[0] + 1
    print (s)