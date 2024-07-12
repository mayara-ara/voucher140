#Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de 
#notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente 
#média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
#fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
#como nota de aprovação
notas = []
entrada_valida=True

print("Digite suas notas.insira um valor fora do intervalo de 0 a 10 para terminar")

while entrada_valida:
    entrada= input("digite uma nota (0-10)ou um valor invalido para terminar: ")

    try:
        nota=float(entrada)

        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            entrada_valida= False

    except ValueError:
        entrada_valida = False
if notas:
    media=sum(notas) / len (notas)
    print(f"A media aritimética das notas é: {media:.2f}")   
else:
    print("nenhum nota valida for inserido") 


