####exercicio número 14 lista 3####
numero1 = int (input('Primeiro numero: '))
numero2= int(input("segundo numero: "))

if numero1 == numero2:
    print("Números iguais:", numero1)
else:
    # Verifica qual é o maior número
    if numero1 > numero2:
        maior_numero = numero1
    else:
        maior_numero = numero2

    # Calcula a diferença entre os números
    diferenca = abs(numero1 - numero2)

    # Imprime o maior número e a diferença entre eles
    print("O maior número é:", maior_numero)
    print("A diferença entre os números é:", diferenca)