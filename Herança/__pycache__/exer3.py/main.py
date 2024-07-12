from Ingresso import Ingresso
from Ingressovip import Ingressovip

ingresso1 = Ingresso(preco=100.00, setor='Pista')
ingressoVIP1 = Ingressovip(preco=300.00, setor='VIP', camarote=True, open_bar=True, open_food=False, estacionamento=True)

print(ingresso1)
ingresso1.alterar_preco(120.00)
print(f'Novo preço: R${ingresso1.preco:.2f}')
print(ingresso1.mostrar_setor())

print(ingressoVIP1)
print(ingressoVIP1.pegar_bebida())
print(ingressoVIP1.acessar_camarote())
