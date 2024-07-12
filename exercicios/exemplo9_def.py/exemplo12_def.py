#crie uma função que receba uma lista como argumento,os valores da lista devem ser numericos, por fim retorne a media desses valores.
def calcular_media (lista):
    if not lista:
        return 0
    soma = sum (lista)
    quantidade = len (lista)
    media = soma / quantidade
    return media

valores = [10,20,30,40,50]
media= calcular_media (valores)
print(f"a media dos valores é: {media}")