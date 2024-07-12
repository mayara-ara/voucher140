# Definindo o dicionário corretamente
amigos = {
    "amigos1": "mayara",
    "amigos2": "Erika",
    "amigos3": "vanda",
    "amigos4": "suellen"
}

#for chave, nome in amigos.items():
    #print(f"{chave} tem {nome}")

#nome = input("Digite o nome de um amigo: ")

#if nome in amigos.values():
    #print(True)
#else:
    #print(False)

#tradução={
    #"thank you": "gracias",
    #"bye": "adios",
    #"hello": "hola"
#}
#n=input("digite uma paravra em ingles ")

#for n in tradução:
    #print(f"A tradução é:  {tradução[n]}")
#else:
    #print("não esta no dicionario")
lista_amigos=[(nome,idade)
for nome,idade in amigos.items()]
print("lista de amigos em tupla: ",lista_amigos)
