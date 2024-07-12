##exercicio 13 da lista ####
#Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
#de 0 até N em ordem decrescente
N = int(input("Digite um número inteiro positivo N: "))
if N < 0:
    print("O número fornecido não é positivo.")
else:
    print("Números naturais de 0 até", N, "em ordem decrescente:")
    
    for num in range(N, -1, -1):
        print(num)