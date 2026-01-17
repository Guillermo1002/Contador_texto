#Programa para contar palabras en un archivo de texto
from nt import read
import re
import os
from collections import Counter

archivo = input("Introduce la ruta de texto (o solo el nombre si está en la misma carpeta): ")

if not os.path.dirname(archivo):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(script_dir, archivo)

try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("El archivo especificado no existe.")
    exit(1)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit(1)

palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)

print("\n")
print("Texto citado: " + texto)
print(f"total palabras: {total_palabras}")

contador = Counter(palabras)
mas_comunes = contador.most_common(100)
print("Palabras mas frecuentes: ")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")
