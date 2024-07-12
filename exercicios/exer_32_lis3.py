###Exercicio 32 da lista 3###. 

categoria_idade=float(input("digite a idade do nadador: "))
if 5 <= categoria_idade <=7 :
    mensagem = "infantil A!"
elif 8 <= categoria_idade <= 10:
    mensagem = "infantil B!"
elif 11 <= categoria_idade <= 13:
    mensagem= "juvenil A!"
elif 14 <= categoria_idade <= 17:
    mensagem="juvenil B!"
else:
    mensagem = "Sênior maior de 18 anos!"
print("Categoria do nadador:", mensagem)