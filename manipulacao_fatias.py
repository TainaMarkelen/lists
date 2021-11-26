#fatia de lista, pegar um pedaço
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#o comprimento é o final menos o começo
print (primos [1:2])

#começa pelo 5 e continua até dá 5, resultado de 7 - 2
print (primos[2:7])
#a lista inicial não é alterada, é criada uma nova lista
print (primos[0:12])
#para pegar desde o início não é preciso citar o primeiro
print (primos[:12])
#o mesmo para ir até o final
print(primos[12:])
#todos, a partir da posição 1
print(primos[1:])

#guardar em uma nova variável
final = primos[12:]
print (final)