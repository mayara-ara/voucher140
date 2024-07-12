####exercicio da 38 da lista 3###
peso=float(input("digite o peso da pesoa em KG:  "))
altura =float(input("digite a altura da pessoa em metros: "))
imc = peso / (altura ** 2)

classificacao= ""
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "saudável"
elif 25.0 <= imc <= 29.9:    
    classificacao = "Peso em excesso"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade grau 1"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade grau 2(severa)"
else:
    classificacao = "obesidade grau 3(mórbida)"

print("o imc da pessoa é: ",imc)
print("clasificacao: ",classificacao)
