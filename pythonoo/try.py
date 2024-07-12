i = 0
soma = 0
while i < 10:
    try:
        x = int(input("digite um numero: "))
        soma += x
        i +=1
    except:
        print("Valor invalido!! Tente Novamente")

print(soma)