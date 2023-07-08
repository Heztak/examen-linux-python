# Importa las bibliotecas necesarias
import requests  # Para hacer solicitudes HTTP
import csv  # Para trabajar con archivos CSV
import collections  # Para contar elementos en una lista
import os  # Para trabajar con el sistema operativo
import re  # Para trabajar con expresiones regulares

# Hace una solicitud GET al endpoint y guarda la respuesta en la variable 'response'
response = requests.get('https://dummyjson.com/quotes')

# Convierte la respuesta JSON en un diccionario de Python y lo guarda en la variable 'data'
data = response.json()

# Abre (o crea) el archivo 'endpoint.csv' en modo escritura ('w')
with open('endpoint.csv', 'w', newline='') as f:
    # Crea un objeto writer de CSV que escribirá en el archivo 'f' usando tabulaciones como delimitador
    writer = csv.writer(f, delimiter='\t')
    # Itera sobre cada elemento en la lista de citas en 'data'
    for item in data['quotes']:
        # Escribe una fila en el archivo CSV con el autor y la cita del elemento actual
        writer.writerow([item['author'], item['quote']])

# Crea una lista vacía para almacenar las palabras
words = []
# Define una lista de palabras que serán excluidas
excluded_words = ['a', 'an', 'the', 'and', 'or', 'but', 'is', 'it', 'this', 'that', 'on', 'was', 'by', 'of', 'to', 'in', 'with', 'as', 'for', 'are']
# Itera sobre cada elemento en la lista de citas en 'data'
for item in data['quotes']:
    # Itera sobre cada palabra en la cita del elemento actual
    for word in re.findall(r'\b\w+\b', item['quote']):
        # Si la palabra en minúsculas no está en la lista de palabras excluidas, la agrega a la lista de palabras
        if word.lower() not in excluded_words:
            words.append(word.lower())

# Crea un objeto Counter a partir de la lista de palabras
counter = collections.Counter(words)
# Obtiene las 10 palabras más comunes y las guarda en 'top_ten'
top_ten = counter.most_common(10)

# Crea un nombre de archivo a partir de las 10 palabras más comunes, unidas por guiones bajos, y le agrega la extensión '.txt'
filename = '_'.join(word for word, count in top_ten) + '.txt'
# Abre (o crea) el archivo con el nombre generado en modo escritura ('w')
with open(filename, 'w') as f:
    pass  # No escribe nada en el archivo
# Cambia los permisos del archivo a 400 (solo lectura para el propietario)
os.chmod(filename, 0o400)
