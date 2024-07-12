##Exercicio 11 da lista 4##
#Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 
#primeiros números pares.
soma = 0
contador_pares = 0
num = 0

while contador_pares < 50:
    if num % 2 == 0:
        soma += num
        contador_pares += 1
    num += 1

print("A soma dos 50 primeiros números pares no intervalo de 0 a 100 é:", soma)