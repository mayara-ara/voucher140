def imprimir_lista_numerada (lista):
    for i, elementos in enumerate (lista,start=1):
        print(f"{i}.{elementos}")


frutas= ["pera","uva","maça","salada mista"]
imprimir_lista_numerada(frutas)