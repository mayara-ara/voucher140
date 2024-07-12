base_maior=float(input("digite a base maior do trapezio: "))
base_menor=float(input("digite a base menor do trapezio: "))
altura=float(input("digite a altura do trapezio:"))

if base_maior <=0 or base_menor <=0 or altura <=0:
        print("o valor informado deve ser positivo ")
else:
        area=((base_maior + base_menor)*altura)/2
        print("Area do trapezio e:",area)