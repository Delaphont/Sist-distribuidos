import json

input_file_path = 'part-00000'
output_file_path = '../almacen/datos.json'  # Puedes cambiar el nombre del archivo según tus preferencias

data_list = []  # Lista para almacenar los datos

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        # Separa la palabra y la lista de documentos y frecuencias
        word, doc_list_str = line.strip().split('\t')
        
        # Elimina los corchetes y espacios y divide la lista en pares (documento, frecuencia)
        doc_list = [tuple(map(str.strip, pair.strip('()').split(','))) for pair in doc_list_str.split(') (')]
        
        # Crea un diccionario con la información
        data = {'word': word, 'documents': doc_list}
        
        # Agrega el diccionario a la lista
        data_list.append(data)

# Escribe la lista de datos en un archivo JSON
with open(output_file_path, 'w') as output_file:
    json.dump(data_list, output_file, indent=2)

print(f'Los datos se han almacenado en {output_file_path}')