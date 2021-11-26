#strings e inteiros são imutáveis
a = "banana"
b = "banana"
c = "maçã"

#isso irá indicar se as variáveis A e B estão apontando pro mesmo endereço na memória, mesmo objeto
if a is b:
    print ("A é B")
    
if a is c:
    print ("A é C")
    
#listas são objetos mutáveis
d = [81,82,83]
e = [81,82,83]

#apesar de serem iguais elas não irão mais apontar para o mesmo endereço, cada uma ocupa um lugar diferente na memória, só depois as listas apontam para o mesmo conteúdo
if d is e:
    print ("D é E")
else:
    print ("D não é E")
    
#por o conteúdo ser igual, se for feita uma comparação, a resposta será verdadeira
if d == e:
    print("D é igual a E")
    
    
#repetições
origilist = [45,76,34,65]

#criação de uma lista de listas
print ([origilist] * 3)

#a nova listá em um novo endereço, mas está apontando para os objetos da lista original
newlist = [origilist] * 3

#se alterarmos a lista original
origilist[1] = 99
print (origilist)

#a new list também será alterada, apesar de estar em outra memória, pois ainda aponta para os mesmos objetos
print(newlist)