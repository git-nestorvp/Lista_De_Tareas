class Gasto:
    def __init__(self, monto, categoria):
        self.monto = monto
        self.categoria = categoria

class ControlDeGastos:
    def __init__(self):
        self.gastos = []

    def agregar_gasto(self, monto, categoria):
        gasto = Gasto(monto, categoria)
        self.gastos.append(gasto)

    def total_gastos(self):
        return sum(g.monto for g in self.gastos)

    def listar_gastos(self):
        return [(g.monto, g.categoria) for g in self.gastos]

