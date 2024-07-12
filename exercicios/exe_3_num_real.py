####exercicio número 10 lista 3####
import math

numero = float(input("leia um numero: "))

if numero >= 0:
    numero = math.sqrt(numero)
    print('raiz quadrada.',numero)
else: 
    numero = numero**2
print('numero quadrado.',numero)
