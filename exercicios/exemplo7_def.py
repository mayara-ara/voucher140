def calcular_salario(horas_trabalhadas, taxa_por_hora):
    limite_horas_normais = 40
    taxa_hora_extra = 1.5  # 50% a mais

    if horas_trabalhadas <= limite_horas_normais:
        salario = horas_trabalhadas * taxa_por_hora
    else:
        horas_extras = horas_trabalhadas - limite_horas_normais
        salario_normal = limite_horas_normais * taxa_por_hora
        salario_horas_extras = horas_extras * taxa_por_hora * taxa_hora_extra
        salario = salario_normal + salario_horas_extras

    return salario

# Exemplo de uso
horas_trabalhadas = 45
taxa_por_hora = 20
salario = calcular_salario(horas_trabalhadas, taxa_por_hora)
print(f"Salário para {horas_trabalhadas} horas trabalhadas: R$ {salario:.2f}")
