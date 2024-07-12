def calcular_excesso_e_multa(peso_peixe):
    limite_peso = 50
    valor_multa_por_quilo = 4.00

    excesso =max(0,peso_peixe - limite_peso)
    multa = excesso * valor_multa_por_quilo

    print(f"peso total: {peso_peixe}kg")
    if excesso > 0:
        print(f"Excesso de peso: {excesso}")
        print(f"Valor da multa: {multa}")

    else:
        print(f"Não ha,excesso de peso.")
        print(f"Valor da multa R$0.00")

peso_peixe = float(input("Digite o peso total de peixe em (kg)"))
calcular_excesso_e_multa(peso_peixe)