###exercicio 1 da lista 4 while###
#Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, 
#iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após contagem.
import time

contador = 10
while contador >= 0:
    print(contador)
    contador -= 1
    time.sleep(1)

print("fim da contagem regresiva!")

