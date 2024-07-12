#####exercicio numero 26 lista ####
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))


if A < B + C and B < A + C and C < A + B:
    
    if A == B == C:
        print("O triângulo é Equilátero")
    elif A == B or A == C or B == C:
        print("O triângulo é Isósceles")
    else:
        print("O triângulo é Escaleno")
else:
    print("Não é um triângulo")