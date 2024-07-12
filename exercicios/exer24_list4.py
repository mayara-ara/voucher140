#Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 
#ou 5.

soma_multiplos = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma_multiplos += i

print(f"A soma de todos os múltiplos de 3 a 5 abaixo de 1000 é: {soma_multiplos}")