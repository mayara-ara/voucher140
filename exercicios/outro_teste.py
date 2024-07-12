numero=[24,12,33,99,7,8.18,10.5,54]

print("menor número: ",min(numero))
print("maior numero: ",max(numero))
print("soma: ",sum(numero))
print("media: ",sum(numero) / len(numero))

lista_ordenada= sorted(numero)
print(lista_ordenada)
print(numero[1])
indice= numero.index(7)
print(indice)
numero.insert(0,"mayara")
numero.insert(2,1993)
print(numero)
numero.append("segundona")
print(numero)