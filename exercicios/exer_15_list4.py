##exercicio 15 da lista 4##
###Crie um programa que leia um número inteiro positivo par N e imprima todos os números
#pares de 0 até N em ordem decrescente.
N = int(input("Digite um número inteiro positivo N: "))
if N <= 0 or N % 2 != 0:
    print("O número inteiro positivo par.")
else:
    print("Números naturais de 0 até", N, "em ordem decrecente:")
    
    for num in range(N,-1,-2):
        print(num)
