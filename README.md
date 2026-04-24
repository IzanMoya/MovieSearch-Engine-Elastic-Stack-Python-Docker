# 🎬 MovieSearch Engine: Elastic Stack + Python

Este proyecto es un motor de búsqueda y análisis de datos cinematográficos utilizando el **Elastic Stack (ELK)**. Permite indexar miles de películas desde un dataset de TMDB y visualizarlas en paneles interactivos.

## 🚀 Arquitectura del Proyecto
El sistema sigue un flujo de datos moderno:
1. **Dataset**: Archivo CSV con +10,000 películas (TMDB).
2. **Ingesta**: Script en **Python** que limpia los datos con **Pandas** y los envía a la base de datos.
3. **Almacenamiento**: **Elasticsearch** (NoSQL) para búsquedas ultrarrápidas.
4. **Visualización**: **Kibana** para la creación de dashboards de analítica.

---

## 🛠️ Tecnologías Utilizadas
* **Elasticsearch 8.12.0** (Motor de búsqueda)
* **Kibana 8.12.0** (Visualización)
* **Docker & Docker Compose** (Containerización)
* **Python 3.10+** (Scripting y ETL)
* **Pandas** (Procesamiento de datos)

---

## 📦 Instalación y Configuración

### 1. Levantar la infraestructura
Asegúrate de tener Docker instalado y ejecuta:
```bash
docker-compose up -d
