##exercicio 2 da lista 4 while##
#Crie um programa que determine o mostre os 5 primeiros números ímpares, considerando 
#números maiores que 0#

n = 13
contador_impares = 0

while contador_impares < 5:
    if n % 2 != 0:
        print(n)
        contador_impares += 1
    n += 1
print("fim!")