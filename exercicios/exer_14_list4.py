###exercicio 14 lista 4##
###Crie um programa que leia um número inteiro positivo par N e imprima todos os números 
##pares de 0 até N em ordem crescente.
N = int(input("Digite um número inteiro positivo N: "))
if N <= 0 or N % 2 != 0:
    print("O número inteiro positivo par.")
else:
    print("Números naturais de 0 até", N, "em ordem crescente:")
    
    for num in range(0,N + 1, 2):
        print(num)