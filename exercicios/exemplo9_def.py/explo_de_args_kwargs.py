#args(cria valores e salva em tuplas)
#kwargs(cria valores e salva no dicionario)
def imprime_nome(nome1,nome2,*args):
    return nome1,nome2,args
objecto= imprime_nome("fabio","jonas","maisum","maisoutro")

print(objecto)
print(type(objecto))