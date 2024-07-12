#exercicio 31 da lista 3###

distancia_km = float(input("Digite a distância percorrida em Km: "))
litros_consumidos = float(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo_km_por_litro = distancia_km / litros_consumidos

if consumo_km_por_litro < 8:
    mensagem = "Venda o carro!"
elif 8 <= consumo_km_por_litro <= 14:
    mensagem = "Econômico!"
else:
    mensagem = "Super econômico!"

print("O consumo do carro é de {:.2f} Km/l. {}".format(consumo_km_por_litro, mensagem))