###exercicio 8 da lista 4###

numeros = []
contador = 0

while contador < 10:
    num = float(input(f"insira o {contador +1}º número: "))
    if num < 0:
        continue
    else:
        numeros.append(num)
        contador += 1

media = sum(numeros) / 10

print (media)