#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse 
#número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
#1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
num=int(input("digite um numero: "))
divisiveis = []
i = num
while i > 0:
    if i == num:
        i = i - 1
    elif num % i == 0:
        divisiveis.append(i)
        i = i - 1
    else:
        i = i - 1

print(divisiveis)
print(sum(divisiveis))

