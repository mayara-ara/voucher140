#crie uma função que retorne uma lista com valor padrão.para esta função,consideraremos como argumento
#de entrada a quantidade de elementos e o valor padrao a ser atribuído a todos eles.exemplo de retorno:
#[1,1,1,1,1,1,1,1]
#["A","A","A","A"]

def criar_lista(valor_padrao,quatidade):
    return [valor_padrao] * quatidade


lista_numeros = criar_lista (1,8)
lista_letras = criar_lista("A",4)

print(lista_numeros)
print(lista_letras)