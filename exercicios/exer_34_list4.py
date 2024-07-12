lista = []
impar = 0
par = 0

i = 0
while i < 9:
    num = int(input("Digite um número: "))
    # Validar se é par ou ímpar
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    lista.append(num)
    i = i + 1

print(lista)
print("Pares:", par)
print("Ímpares:", impar)