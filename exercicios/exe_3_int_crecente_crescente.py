####exercicio número 15 lista 3####
numero1 = int (input('Primeiro numero: '))
numero2= int(input("segundo numero: "))
numero3=int(input("terceiro numero: "))

if numero1 < numero2 < numero3:
    diferenca = numero3 - numero1
    print("Os números", numero1, ",", numero2, "e", numero3, "estão em ordem crescente.")
    print("A diferença entre eles é:", diferenca)
else:
    print("Os números", numero1, ",", numero2, "e", numero3, "não estão em ordem crescente.")
    