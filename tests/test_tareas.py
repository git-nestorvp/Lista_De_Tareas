import sys
import os

# Esto agrega la carpeta principal del proyecto al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora puedes importar las clases
from gasto import Gasto

def test_agregar_gasto():
    gasto = Gasto(100, "Comida")
    assert gasto.monto == 100
    assert gasto.categoria == "Comida"
