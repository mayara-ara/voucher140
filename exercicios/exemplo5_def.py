def soma_imposto (taxa_imposto,custo):
    novo_custo=custo + (custo * (taxa_imposto/100))
    return novo_custo

taxa= 10 #10% de imposto
custo_inicial=200
custo_final=soma_imposto(taxa,custo_inicial)

print(f"custo inicial é: {custo_inicial}")
print(f"com a taxa de imposto: {taxa}, o custo final é {custo_final}")