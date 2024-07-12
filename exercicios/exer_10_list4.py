##Exercicio 10 da lista 4###

N = int(input("Digite um número inteiro N: "))

numero_impar = 1
print(f"Os {N} primeiros números naturais ímpares são: ")
for _ in range(N):
    print(numero_impar)
    numero_impar += 2 