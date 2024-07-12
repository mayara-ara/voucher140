
notas = {
    "nota1": 10,
    "nota2": 7,
    "nota3": 8,
    "nota4": 6
}

media = sum(notas.values()) / len(notas)

print(f"Média das notas iniciais: {media:.2f}")

while True:
    try:
        nota = int(input("Digite uma nova nota (ou digite uma letra para sair): "))
        print(f"Nova nota: {nota}, Média das notas iniciais: {media:.2f}")
    except ValueError:
        print("Saindo...")
        break
