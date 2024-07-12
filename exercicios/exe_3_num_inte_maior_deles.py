####exercicio número 13 lista 3####
numero1 = int (input('Primeiro numero: '))
numero2= int(input("segundo numero: "))

if numero1 > numero2:
    maior_numero = numero1
elif numero2 > numero1:
    maior_numero = numero2
else:
    print("Os números são iguais.")
    # Se os números forem iguais, não há diferença
    exit()

# Calcula a diferença entre os números
diferenca = abs(numero1 - numero2)

# Imprime o maior número e a diferença entre eles
print("O maior número é:", maior_numero)
print("A diferença entre os números é:", diferenca)