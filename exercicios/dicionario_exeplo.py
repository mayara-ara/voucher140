pessoa={
    "nome": "mayara" ,
    "idade": "30" ,
    "cidade_natal": "campo grande",
    "profissao": "estudante"
    }
nome_pessoa=pessoa['nome']
idade_pessoa=pessoa['idade']
print("nome: ",nome_pessoa)
print("idade: ",idade_pessoa)

pessoa["idade"] = 30
print("pessoa: ",pessoa)

pessoa["email"]="mayara18.santos@gmail.com"
pessoa["telefone"]="67998512134"
print("atualizado: ",pessoa)
