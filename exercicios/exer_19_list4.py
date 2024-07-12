###Exercicio 19 da lista 4###
#Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um 
#dos algarismos que compõem o número

numero = int(input("Digite um numero entre 100 e 9999: "))

if 100 <= numero <= 9999:
    numero_str = str (numero)
    print("os algorismo que compõem o número",numero,"são: ")
    for algorismo in numero_str:
        print(algorismo)
else:
    print("o numero digitado esta fora do intervalo valido")