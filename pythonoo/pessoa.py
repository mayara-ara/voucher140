class Pessoa:
    def __init__(self,id=0,nome=""):
        self.id =id
        self.nome = nome

    def hello(self):
        print("Ola")

pes1= Pessoa()
print(pes1.id)

print("Bom dia!!!")
name= input("Digite seu nome: ")

pes1.nome = name

pes1.hello()