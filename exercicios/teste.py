#exercicio 20####

n1=float(input("DIGITE n1: "))
n2=float(input("DIGITE n2: "))
n3=float(input("DIGITE n3: "))

media=(((n1 * 1 ) +(n2 * 1 ) + (n3 * 2))/4 )* 10
print(media)
if media >=60:
    print("aprovado")
elif media < 60 and media >=30:
    print("recuperação!!!!")
else:
    print("REPROVADO")