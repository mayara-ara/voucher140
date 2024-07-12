###exercicio 12 da lista 4###
#Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
#de 0 até N em ordem crescente.
N = int(input("Digite um número inteiro positivo N: "))

if N < 0:
    print("O número fornecido não é positivo.")
else:
    print("Números naturais de 0 até", N, "em ordem crescente:")
    
    numeros_naturais = list(range(N + 1))
    numeros_naturais.sort()
    for num in numeros_naturais:
        print(num)