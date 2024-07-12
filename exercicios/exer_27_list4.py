#Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do 
#Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

A=int(input("digite o valor inicial A: "))

fatorial = 1

sequencia = ""

for i in range(A,0,-1):
    fatorial *=i 
    sequencia += str(i)
    if i != 1:
        sequencia += "x"

print(f"{A}! = {sequencia} = {fatorial}")