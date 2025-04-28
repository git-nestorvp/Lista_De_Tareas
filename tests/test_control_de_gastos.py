import sys
import os

# Esto agrega la carpeta principal del proyecto al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora puedes importar las clases
from control_de_gastos import ControlDeGastos

def test_agregar_gasto():
    control = ControlDeGastos()
    control.agregar_gasto(100, "Comida")
    assert len(control.gastos) == 1
    assert control.gastos[0].monto == 100
    assert control.gastos[0].categoria == "Comida"

def test_total_gastos():
    control = ControlDeGastos()
    control.agregar_gasto(100, "Comida")
    control.agregar_gasto(50, "Transporte")
    assert control.total_gastos() == 150

def test_listar_gastos():
    control = ControlDeGastos()
    control.agregar_gasto(100, "Comida")
    control.agregar_gasto(50, "Transporte")
    assert control.listar_gastos() == [(100, "Comida"), (50, "Transporte")]
