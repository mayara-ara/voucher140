####exercicio 24 da lista 3####

base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

if base_maior <= 0 or base_menor <= 0 or altura <= 0:
    print("Os valores inseridos devem ser positivos.")
else:
    area = ((base_maior + base_menor) * altura) / 2
    print("A área do trapézio é:", area)














    