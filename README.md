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
---

### 2. Las 3 Capturas que debes poner (Guía visual)

Para que el README se vea profesional, no pongas capturas de toda tu pantalla. Usa la herramienta de recorte de Windows (`Win + Shift + S`) para capturar solo lo importante:

1.  **Captura del Dashboard (La más importante):** Ve a tu Dashboard de Kibana, pulsa en "Full Screen" o simplemente recorta el área donde están tus gráficos. Es la "foto de portada" de tu proyecto.
2.  **Captura de los Contenedores:** Abre **Docker Desktop**. Captura la fila donde se ven `elasticsearch` y `kibana` con el icono verde de "Running". Esto demuestra que sabes gestionar infraestructura.
3.  **Captura de la Terminal (Opcional pero pro):** Una captura de tu terminal de VS Code después de ejecutar el script, donde se vea el mensaje: *"¡Todas las películas han sido indexadas correctamente!"*. Esto prueba que el código funciona.

### 3. Bonus: El archivo `.gitignore`

Crea un archivo llamado `.gitignore` (con el punto delante) en tu carpeta raíz para que GitHub no se llene de archivos basura. Pon esto dentro:

```text
# Entornos virtuales
.venv/
__pycache__/

# Datos (No se suben archivos grandes a GitHub)
data/*.csv

# Configuración de VS Code
.vscode/
