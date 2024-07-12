###Exercicio 18 da lista 4####
#Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A 
#quantidade de números a serem lidos deve será fornecida pelo usuário

quantidade_numeros = int(input("Digite a quantidade números a sere lidos: "))
maior_numero = None

for _ in range(quantidade_numeros):
    numero = float(input("Digite um número: "))
    
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print("O maior número fornecido é:", maior_numero)