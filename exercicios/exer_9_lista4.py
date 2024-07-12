###Exercicio 9 da lista 4 while###


for num in range(10):
    n = int(input(f"Digite o {num +1}º número: "))
    numeros.append(n)
    
    menor = min(numeros)
    maior = max(numeros)
    
    print(menor)
    print(maior)