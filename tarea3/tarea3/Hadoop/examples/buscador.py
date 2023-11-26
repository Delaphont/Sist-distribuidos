import json

class Buscador:
    def __init__(self, datos):
        # Crea un diccionario con la estructura {palabra: [(documento, coincidencias), ...]}
        self.datos = {item['word']: item['documents'] for item in datos}

    def buscar(self, consulta):
        consulta = consulta.lower()

        if consulta not in self.datos:
            return f"No se encontró la palabra '{consulta}'."

        resultados = []

        # Obtener los documentos ordenados por coincidencias (de mayor a menor)
        documentos_ordenados = sorted(self.datos[consulta], key=lambda x: int(x[1]), reverse=True)

        # Obtener los 5 mejores resultados
        for doc_id, coincidencias in documentos_ordenados[:5]:
            url = f'https://es.wikipedia.org/wiki/{doc_id}'
            resultados.append((url, doc_id, int(coincidencias)))

        result = f"Resultados para '{consulta}':\n"
        for url, doc_id, frecuencia in resultados:
            result += f'Documento: {doc_id}, Frecuencia: {frecuencia}, URL: {url}\n'

        return result

if __name__ == '__main__':
    # Lee el archivo JSON con el índice invertido
    with open("almacen/datos.json", "r") as f:
        datos = json.load(f)

    buscador = Buscador(datos)

    while True:
        consulta = input("Ingrese su búsqueda (o presione Enter para salir): ")
        if not consulta:
            break

        resultado = buscador.buscar(consulta)
        print(resultado)