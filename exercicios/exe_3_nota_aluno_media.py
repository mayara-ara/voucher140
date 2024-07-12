####exercicio número 16 lista 3####
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    
    media = (nota1 + nota2) / 2
    
    print("A média das notas é:", media)
else:
    print("Pelo menos uma das notas não é válida. As notas devem estar entre 0 e 10.")