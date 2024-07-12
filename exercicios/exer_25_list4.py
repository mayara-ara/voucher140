#Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando 
#for informada a idade 0), e calcule a idade média desse grupo

idades = []
print("Digite as idades dos indivíduos. Para terminar, digite 0.")

while True:
    idade = int(input("Digite a idade: "))

    if idade == 0:
        break
    
    idades.append(idade)

if idades:
    media = sum(idades) / len(idades)
    print(f"A idade média do grupo é: {media:.2f}") 
else:
    print("Nenhuma idade válida foi inserida.")