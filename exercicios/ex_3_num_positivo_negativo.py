####exercicio número 11 lista 3####
import math

# Solicita ao usuário um número
numero = float(input("Digite um número: "))

# Calcula o quadrado do número
quadrado = numero ** 2

if numero >= 0:
    # Calcula a raiz quadrada do número
    raiz_quadrada = math.sqrt(numero)
    print("O quadrado de", numero, "é", quadrado)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("Não é possível calcular a raiz quadrada de um número negativo")
