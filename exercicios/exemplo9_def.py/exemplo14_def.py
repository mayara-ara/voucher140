#crie uma função que receba como argumento a pot~encia eletrica de determinado aparelho e o tempo ligado e retorne
#o consulmo em KWh em seduida chame outra função para calcular a conta de energia,levando em consederação o consumo e o valor do KWh
#como argumento
def calcular_consumo(potencia_watts, tempo_horas):
    """
    Calcula o consumo de energia em kWh.
    
    Args:
    potencia_watts (float): Potência elétrica do aparelho em watts.
    tempo_horas (float): Tempo que o aparelho ficou ligado em horas.
    
    Returns:
    float: Consumo de energia em kWh.
    """
    consumo_kwh = (potencia_watts / 1000) * tempo_horas
    return consumo_kwh

def calcular_conta(consumo_kwh, valor_kwh):
    """
    Calcula o valor da conta de energia.
    
    Args:
    consumo_kwh (float): Consumo de energia em kWh.
    valor_kwh (float): Valor do kWh em reais.
    
    Returns:
    float: Valor da conta de energia.
    """
    conta = consumo_kwh * valor_kwh
    return conta

# Exemplo de uso
potencia = 1500  # potência em watts
tempo = 5        # tempo em horas
valor_kwh = 0.50  # valor do kWh em reais

consumo = calcular_consumo(potencia, tempo)
conta = calcular_conta(consumo, valor_kwh)

print(f"Consumo: {consumo} kWh")
print(f"Conta de energia: R$ {conta:.2f}")
