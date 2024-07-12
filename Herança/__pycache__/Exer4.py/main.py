from Passagem import Passagem
from Passagem1 import Passagem1
from PassagemAviao import PassagemAviao
from PassagemBus import PassagemBus

passagem_aviao = PassagemAviao(500, "12A", "B4", False)
print(passagem_aviao)

info_checkin = passagem_aviao.Chegar_checkin(True)
print(info_checkin)


passagem_aviao.decolar()

passagem_bus = PassagemBus(150, "21B", "ABC-1234", False)
print(passagem_bus)

passagem_bus.abastecer()

