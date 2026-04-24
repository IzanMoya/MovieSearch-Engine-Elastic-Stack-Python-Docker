from elasticsearch import Elasticsearch, helpers
import pandas as pd

# 1. Conectar a Elastic en Docker (Cambiado a http)
es = Elasticsearch("http://localhost:9200")

# Funcion para cargar los datos
def indexar_peliculas_csv():
    print("Leyendo archivo CSV...")
    
    # 2. Leer el CSV con pandas (Corregido el nombre a tmdb)
    df = pd.read_csv('data/tmdb_movies_data.csv')

    # 3. Limpieza: ElasticSearch falla si hay valores NaN en el csv
    df = df.fillna('')

    # 4. Convertir las filas del CSV en una lista de diccionarios
    peliculas = df.to_dict(orient='records')

    # 5. Preparar el formato masivo (Bulk)
    print("Preparando los datos para Elasticsearch...")
    acciones = [
        {
            "_index": "peliculas",
            "_source": peli  # Corregido a singular: _source
        }
        for peli in peliculas
    ]

    # 6. Enviar todo a la vez
    print(f"Subiendo {len(acciones)} peliculas a Elastic. Esto puede tardar unos segundos...")
    helpers.bulk(es, acciones)
    print("¡Todas las peliculas han sido indexadas correctamente!")

indexar_peliculas_csv()