# 🎬 MovieSearch Engine: Elastic Stack + Python & Docker

Este proyecto es un motor de búsqueda y análisis de datos cinematográficos de extremo a extremo utilizando el **Elastic Stack (ELK)**. Permite extraer, limpiar, indexar de forma masiva miles de películas desde un dataset de TMDB y visualizarlas en paneles interactivos.

## 🚀 Arquitectura del Proyecto y Fases

El sistema sigue un flujo de datos moderno, abarcando todo el ciclo de vida del dato:

1. **Fase de Infraestructura (DevOps):** Uso de **Docker y Docker Compose** para desplegar contenedores de Elasticsearch (motor) y Kibana (visualización) sin instalaciones locales pesadas.
2. **Ingeniería de Datos (ETL):** Script en **Python** utilizando **Pandas** para extraer datos crudos de un CSV (+10.000 registros), limpiar valores nulos y enviarlos mediante *Bulk Insert*.
3. **Almacenamiento (NoSQL):** Indexación en **Elasticsearch**, optimizado para búsquedas a la velocidad del rayo y estructuras JSON.
4. **Inteligencia de Negocio (BI):** Creación de *Data Views* e inspección en **Kibana** para construir Dashboards interactivos usando Kibana Lens.

---

## 🛠️ Tecnologías Utilizadas

* **Base de Datos / Motor:** Elasticsearch 8.12.0
* **Visualización / BI:** Kibana 8.12.0
* **Infraestructura:** Docker & Docker Compose
* **Lenguaje y ETL:** Python 3.10+ (Pandas, API oficial de Elasticsearch)

---

## 📊 Dashboard de Análisis

Una vez indexados los datos, Kibana permite realizar análisis profundos transformando datos crudos en información visual. El dashboard principal incluye:

* **Evolución del Cine:** Histograma de lanzamientos por año (intervalos).
* **Distribución:** Gráficos circulares sobre proporciones dentro del catálogo.

<img width="1916" height="439" alt="image" src="https://github.com/user-attachments/assets/96269108-5f38-4008-8349-ede69ced5da7" />

---

## 🔍 Características de Búsqueda

Gracias a Elasticsearch, el motor soporta funcionalidades avanzadas que una base de datos relacional tradicional sufriría para ejecutar:

* **Fuzzy Search (Búsqueda difusa):** Encuentra películas incluso si el usuario comete errores ortográficos (ej. buscar "Intestelar" encuentra "Interstellar").
* **Búsqueda Full-Text:** Indexación rápida y eficiente de títulos y descripciones.

*(Vista de "Discover" en Kibana inspeccionando la estructura de los documentos JSON)*
<img width="1917" height="947" alt="image" src="https://github.com/user-attachments/assets/2196bf7e-5ce1-4c9d-bbbc-a858e42ac0f3" />

---

## ⚙️ Configuración e Infraestructura con Docker

El entorno se gestiona completamente mediante Docker para garantizar que sea reproducible en cualquier máquina, resolviendo dependencias de Java o configuraciones de red complejas.

<img width="1645" height="233" alt="image" src="https://github.com/user-attachments/assets/6e964e5f-465e-4d03-8cd6-6e89bb85596d" />

### Instrucciones de Instalación:

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Clona este repositorio.
3. Levanta la infraestructura ejecutando en tu terminal:
   ```bash
   docker-compose up -d
4. Instala las dependencias de Python (se recomienda un entorno virtual):
   pip install -r requirements.txt
6. Ejecuta el script de ingesta (asegúrate de tener el archivo CSV en la ruta correcta):
   python scripts/indexer.py
