# Proyecto Maverik: Aplicación de Retrieval Augmented Generation (RAG)

Servicio que contiene y gestiona el LLM encargado de generar las respuestas para el usuario.

## Características

- **Alta velocidad**: Gracias a las capacidades asíncronas de FastAPI.
- **Tipado automático**: FastAPI genera automáticamente la documentación de la API basada en los tipos de Python.
- **Validación de datos**: Utiliza Pydantic para validar los datos de entrada de manera sencilla.
- **Documentación automática**: Incluye documentación interactiva utilizando Swagger UI y Redoc.

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn (para ejecutar la aplicación)
- Las dependencias detalladas en el archivo `requirements.txt`

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/abreuerUade/maverik_rag
   cd maverik_rag
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source env/bin/activate  # En Linux/macOS
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**:

   Asegúrate de crear un archivo `.env` o configurar las variables de entorno necesarias para la aplicación.
   Las necesarias son:

   ```bash
   OPENAI_API_KEY=''
   MONGODB_ATLAS_CLUSTER_URI=''
   GOOGLE_API_KEY=''
   GOOGLE_CSE_ID=''
   SERPAPI_API_KEY=''
   FMP_API_KEY=''
   ```

5. **Iniciar la aplicación:**

   Ejecuta el servidor FastAPI usando Uvicorn:

   ```bash
   uvicorn src.main:app --reload
   ```

   Esto iniciará el servidor en `http://127.0.0.1:8000` con recarga automática en caso de cambios en el código.

## Despliegue

Se puede desplegar la aplicación en varios servicios de hosting como:

- **Heroku**
- **AWS Lambda**
- **Google Cloud Run**
- **Render**

Para desplegarla en AWS Lambda, se puede ejecutar el archivo `lambda_script.sh` el cual prepara un archivo .zip para las dependencias y uno para el codigo fuente. Así se pueden desplegar las dependencias en `layers`.
