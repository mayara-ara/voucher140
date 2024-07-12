#exercicio 17 da lista 4###
#Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros 
#números naturais.

n = int(input("digite um numero inteiro e positivo "))
if n <= 0:
    print("numero inteiro positivo ")
else:
    soma = (n * (n + 1 ))//2
    print("a soma dos ",n,"primeiro numero naturais é ",soma)












