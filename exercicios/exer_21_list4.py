#Crie um programa que receba dois números. Calcule e mostre:
#• a soma dos números pares desse intervalo de números, incluindo os números digitados;
#• a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
soma_pares = 0
multiplicacao_impares =1 
soma_pares = 0
multiplicacao_impares = 1
for num in range(num1, num2 + 1):
    if num % 2 == 0:
        soma_pares += num
else:
    multiplicacao_impares *= num
    print(f"Soma dos números pares: {soma_pares}")
    print(f"Multiplicação dos números ímpares: {multiplicacao_impares}")

    