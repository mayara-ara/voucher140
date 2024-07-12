class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0  
    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcularValorTotal(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return self.valor_total

nota_fiscal = Nota_Fiscal(
    numero=12345,
    tipo='Entrada',
    serie=1,
    cnpj='12.345.678/0001-99',
    razao_social='Empresa Exemplo Ltda',
    data='01/07/2024',
    valor_produtos=1000.0,
    icms=180.0,
    frete=50.0,
    ipi=100.0
)

print(f"Número da Nota Fiscal: {nota_fiscal.obterNumero()}")

print(f"Data de Emissão: {nota_fiscal.obterDataEmissao()}")

nota_fiscal.alterarRazaoSocial("Nova Empresa Ltda")
print(f"Nova Razão Social: {nota_fiscal.razao_social}")

valor_total = nota_fiscal.calcularValorTotal()
print(f"Valor Total: R$ {valor_total:.2f}")
