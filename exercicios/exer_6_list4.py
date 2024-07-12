###exercicio 6 da lista 4 de while###

#Escreva um programa que peça ao usuário para digitar 10 valores e some-os

soma = 0
contador = 0
while contador < 10:
    valor = float(input("digite o valor {}º valor ".format(contador + 1)))
    soma += valor 
    contador += 1
print("A soma dos valores é : ",soma)
















