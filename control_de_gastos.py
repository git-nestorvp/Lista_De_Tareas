# control_de_gastos.py

from gasto import Gasto

class ControlDeGastos:
    def __init__(self):
        self.gastos = []

    def agregar_gasto(self, monto, categoria):
        nuevo_gasto = Gasto(monto, categoria)
        self.gastos.append(nuevo_gasto)

    def total_gastos(self):
        return sum(gasto.monto for gasto in self.gastos)

    def listar_gastos(self):
        return [(gasto.monto, gasto.categoria) for gasto in self.gastos]
