##Exercicio 20 da lista 4###
#Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
#informado o número de dados lidos e número de valores pares. O processo termina quando for 
#digitado o número 0

numeros_lidos = 0
numeros_pares = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break
    numeros_lidos += 1
    
    if numero % 2 == 0:
        numeros_pares += 1
print("Número de dados lidos:", numeros_lidos)
print("Número de valores pares:", numeros_pares)