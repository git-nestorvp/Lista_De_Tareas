# funciones.py
from datetime import datetime

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento
