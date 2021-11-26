def compara_assinatura(as_a, as_b):
    cont = 0
    comp = 0
    soma = 0
    absoluto = 0
    
    for i in as_a:
        comp = i - as_b[cont]
        absoluto = abs(comp)
        soma += absoluto
        cont += 1
        
    result = soma / 6
    
    return result

if __name__ == '__main__':
    as_a = [4.20, 0.05, 0.02, 12.81, 2.16, 0.0]
    as_b = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
    
    print (compara_assinatura(as_a, as_b))