#####exercicio 35#####
venda= float(input("digite o valor da casa: "))
if venda >= 100000:
    comisao=(venda * 16 / 100) + 700
    print(comisao)
elif venda < 100000 and venda >= 80000:
    comisao=(venda * 14 / 100) + 650
    print(comisao)
elif venda < 100000 and venda >= 40000:
    comisao=(venda * 14 / 100) + 600
    print(comisao)
elif venda < 100000 and venda >= 20000:
    comisao=(venda * 14 / 100) + 500
    print(comisao)
else:
    comisao=(venda * 14 / 100)
    print(comisao)