def calculotempo(tempo_por_minuto):
    valor_minuto_por_hora = 9.00
    valor_adicional_por_hora = 1.50

    if tempo_por_minuto < 15:
        return 0.00
    
    horas_completas = tempo_por_minuto // 60
    minutos_restantes = tempo_por_minuto % 60

    if minutos_restantes > 0:
        horas_completas += 1

    if horas_completas == 1:
        total = valor_minuto_por_hora
    else:
        total = valor_minuto_por_hora + (horas_completas - 1) * valor_adicional_por_hora

    return total

# Exemplo de uso
tempo_utilizado = int(input("Digite o tempo em minutos: "))
valor_total = calculotempo(tempo_utilizado)
print(f"O valor total a ser pago é: R$ {valor_total:.2f}")
