###exercicio 16 da lista 4####
#Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os 
#números ímpares de 1 até N em ordem crescente

N = int(input("Digite um número inteiro positivo ímpar N: "))
if N <= 0 or N % 2 == 0:
    print("Por favor, digite um número inteiro positivo ímpar.")
else:
    print("Números ímpares de 1 até", N, "em ordem crescente:")
    for num in range(1, N + 1, 2):
        print(num)