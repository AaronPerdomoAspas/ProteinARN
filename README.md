
# NCBI FASTA Downloader

## Descripción

Este proyecto implementa un sistema para descargar archivos FASTA desde la base de datos NCBI utilizando el API de Entrez. El sistema permite especificar identificadores de secuencias directamente o buscar identificadores basados en un término de búsqueda, descargando las secuencias correspondientes en formato FASTA. Posteriormente, los archivos descargados son validados para asegurar su formato correcto, que no estén vacíos y que las secuencias sean válidas. 

El código abarca los siguientes apartados:
- **Extracción**: Recupera los identificadores de secuencias desde el API de NCBI usando una búsqueda basada en términos.
- **Validación**: Se valida que los archivos FASTA descargados tengan un formato adecuado, no estén vacíos, y contengan secuencias correctas.

## Tecnologías Usadas

- **Biopython**: Utilizada para interactuar con el API de Entrez y manipular secuencias FASTA debido a su robustez y facilidad para trabajar con secuencias biológicas.
- **Python estándar**: Manejo de archivos, rutas y excepciones.
- **Ruff**: Linter utilizado para mantener el código limpio y legible, evitando errores comunes.

## Razonamiento

El enfoque implementado se ha centrado en lograr un diseño modularizado que facilite la comprensión, mantenimiento y escalabilidad del código. Cada componente cumple una única función bien definida (principio de responsabilidad única), lo que permite hacer modificaciones sin afectar otras partes del sistema. 

Además, la modularización simplifica la extensión futura del código, facilitando la adición de nuevas funcionalidades, como nuevas formas de validar archivos o soportar diferentes tipos de datos biológicos. Se ha utilizado **Biopython** debido a su soporte robusto para la manipulación de secuencias biológicas y su integración con el API de Entrez, lo que permite una conexión sencilla y fiable con bases de datos como NCBI.

La clase principal de conexión con la API de NCBI, denominada **NCBIConnection** (`Connection`) dentro del código, la cual se encarga de establecer y verificar la conexión con el servicio de NCBI. Esta abstracción permite centralizar la configuración del correo electrónico y cualquier otra validación relacionada con la conexión.

## Estructura de Archivos

```bash
├── conections
│   └── Connection.py       # Clase que maneja la conexión con la API de NCBI
├── config
│   └── Config.py           # Configuración del sistema
├── downloader
│   ├── FastaDownloader.py   # Clase que descarga múltiples archivos FASTA
│   ├── IdFetcher.py         # Clase para buscar identificadores en NCBI
│   ├── SingleFastaDownloader.py # Clase que descarga un único archivo FASTA
│   └── __init__.py
├── orchestrator
│   ├── Main_orchestrator.py # Clase que coordina todo el flujo del sistema
│   └── __init__.py
├── scripts
│   └── main.py              # Script principal para ejecutar el programa
├── utils
│   └── FilePathHelper.py     # Clase auxiliar para manipular rutas de archivos
├── validator
│   ├── FormatValidator.py    # Clase que valida el formato FASTA de los archivos
│   ├── NonEmptyValidator.py  # Clase que valida que los archivos no estén vacíos
│   ├── SequenceValidator.py  # Clase que valida las secuencias de los archivos
│   └── __init__.py
```

### Explicación de Componentes Clave

1. **NCBIConnection**: Responsable de establecer la conexión con el API de NCBI, utilizando el correo electrónico del usuario como identificador. (Este es el nombre que hace referencia a la clase `Connection` en el código).
2. **Config**: Configuración para definir términos de búsqueda, número de archivos a descargar y la ruta del directorio de descarga.
3. **FastaDownloader**: Orquestador de la descarga de múltiples archivos FASTA, usando el identificador obtenido a partir de búsquedas o proporcionados directamente.
4. **IdFetcher**: Permite realizar búsquedas en NCBI y recuperar una lista de identificadores que coinciden con el término de búsqueda.
5. **SingleFastaDownloader**: Descarga un archivo FASTA específico desde NCBI usando un identificador único.
6. **MainOrchestrator**: Clase principal que coordina la conexión, búsqueda, descarga y validación de los archivos FASTA. Este es el punto de entrada del programa.
7. **Validators**: Clases que validan los archivos descargados, asegurándose que sean correctos en términos de formato, contenido y secuencias.
8. **FilePathHelper**: Clase auxiliar para manipular rutas de archivos y extraer solo el nombre del archivo.

## Instrucciones de Uso

1. Clonar este repositorio.
2. Instalar las dependencias, incluyendo **Biopython**. Puedes hacerlo ejecutando:

```bash
pip install biopython
```

3. Configurar el archivo `Config.py` con el correo electrónico y otros parámetros (número de archivos a descargar, identificadores específicos, etc.).
4. Ejecutar el archivo `main.py` desde la carpeta `scripts`:

```bash
python scripts/main.py
```
