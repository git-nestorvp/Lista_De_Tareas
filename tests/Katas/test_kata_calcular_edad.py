import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # Esto hace que Python busque en la raíz del proyecto

from funciones import calcular_edad  # Importamos la función desde funciones.py

def test_calcular_edad():
    # Supongamos que el año actual es 2025
    assert calcular_edad(2000) == 25
    assert calcular_edad(1990) == 35
    assert calcular_edad(2010) == 15
