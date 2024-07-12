from datetime import datetime

class Agenda:
    def __init__(self, dia, mes, ano, anotação=None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotação = anotação

    def validar_data(self):
        try:
            datetime(self.ano, self.mes, self.dia)
            return True
        except ValueError:
            return False
        
    def anotar_tarefas(self, anotação):
        if self.validar_data():
            self.anotação = anotação
            print(f'Tarefa anotada para {self.dia}/{self.mes}/{self.ano}: {self.anotação}')
        else:
            print("Data inválida. Não foi possível anotar a tarefa.")

    def mostrar_anotação(self):
        if self.anotação:
            return f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotação}"
        else:
            return f"Não há anotação para {self.dia}/{self.mes}/{self.ano}."

agenda = Agenda(1, 7, 2024)
if agenda.validar_data():
    agenda.anotar_tarefas("Reunião")
else:
    print("Data inválida. Por favor, insira uma data correta.")

print(agenda.mostrar_anotação())
