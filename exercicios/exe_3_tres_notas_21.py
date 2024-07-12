nota_laboratorio = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
nota_semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
nota_exame_final = float(input("Digite a nota do exame final (0 a 10): "))

if not(0 <= nota_laboratorio <= 10) or not(0 <= nota_semestral <= 10) or not(0 <= nota_exame_final <= 10):
    print("Notas devem estar entre 0 e 10.")
else:
    media_final = (nota_laboratorio * 2 + nota_semestral * 3 + nota_exame_final * 5) / 10

    if 0 <= media_final < 3:
        print("Aluno reprovado.")
    elif 3 <= media_final < 6:
        print("Aluno em recuperação.")
    else:
        print("Aluno aprovado.")



