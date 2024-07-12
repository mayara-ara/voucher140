cargo =(input("digite o cargo: "))

nome = (input("digite e seu nome: "))

idade=int(input("digite sua idade: "))

email:(input("Digite seu email: "))



if(idade >=18):
    print("Parabens voce passou da fase 1 ")
    curso=input("voce possui curso na area? ")
    if curso =="sim":
        print("Parabens voce passou pela 2 fase")
        nota=float(input("Digite a nota da prova"))
        if nota >=7:
            print("Parabens voce passou a fase final")
        else:
            print("Reprovado na fase final")
    else:
        print("obrigado pela participação")
else:
    print("obrigado pela participação")


