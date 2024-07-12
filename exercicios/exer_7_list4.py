###exercicio 7 da lista 4###

#Escreva um programa que leia 10 inteiros e imprima sua média.

soma = 0
contador = 0

while contador < 10:
    valor = int(input("Digite o {}º inteiro: ".format(contador + 1)))
    soma += valor
    contador += 1

media = soma / 10

print("A média dos inteiros é:", media)