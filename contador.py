#Programa para contar palabras en un archivo de texto
import re
import os
from collections import Counter

class ContadorDePalabras:
    def __init__(self):
        self.texto = None
        self.palabras = None
    
    def leer_archivo(self, ruta_archivo):
        
        # Si solo se proporciona el nombre del archivo (sin ruta), buscar en la misma carpeta del script
        if not os.path.dirname(ruta_archivo):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            ruta_archivo = os.path.join(script_dir, ruta_archivo)
        
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                self.texto = f.read()
            return True
        except FileNotFoundError:
            print("El archivo especificado no existe.")
            return False
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False
    
    def contar_palabras(self, num_palabras_comunes=100):
        if not self.texto:
            print("Error: No hay texto cargado. Debes leer un archivo primero.")
            return
        
        # Extraer palabras usando expresiones regulares
        self.palabras = re.findall(r"\w+", self.texto.lower())
        total_palabras = len(self.palabras)
        
        # Mostrar el texto citado y el total de palabras
        print("\n")
        print("Texto citado: " + self.texto)
        print(f"total palabras: {total_palabras}")
        
        # Contar frecuencia de palabras
        contador = Counter(self.palabras)
        mas_comunes = contador.most_common(num_palabras_comunes)
        print("Palabras mas frecuentes: ")
        for palabra, freq in mas_comunes:
            print(f"{palabra}: {freq}")

# Programa principal
if __name__ == "__main__":
    archivo = input("Introduce la ruta de texto (o solo el nombre si está en la misma carpeta): ")
    
    contador = ContadorDePalabras()
    
    if contador.leer_archivo(archivo):
        contador.contar_palabras()
