# ProteinARN

### Descripción de Archivos

1. **`main.py`**: El punto de entrada del programa. Se encarga de coordinar las funciones de los diferentes módulos, procesando los archivos FASTA, realizando la replicación del ADN, transformando el ADN en codones y proteínas, generando tablas y representando gráficamente el proceso.

2. **`manager/`**: Contiene módulos que manejan diferentes aspectos del proceso de replicación:

   - **`FileManager.py`**: Maneja la lectura de archivos FASTA y proporciona métodos para obtener todos los archivos FASTA en un directorio dado.

   - **`ReplicationManager.py`**: Contiene la lógica para realizar la replicación del ADN, implementando métodos que ejecutan la replicación según las teorías conservativa, semiconservativa y dispersiva.

   - **`TransformManager.py`**: Se encarga de transformar la secuencia de ADN replicada en codones y proteínas. Utiliza las clases `CodonTransformer` y `ProteinTransformer` del módulo `transformer`.

   - **`VisualizationManager.py`**: Contiene funciones para representar gráficamente el proceso de replicación en 3D utilizando la biblioteca VPython.

3. **`writer/`**: Módulo que contiene la clase `TableWriter.py`, que crea e imprime tablas en formato de DataFrame para mostrar los resultados de la replicación y transformación del ADN.

3. **`transformer/`**: Contiene módulos que implementan la transformación del ADN en codones y proteínas:

   - **`codon_transformer.py`**: Define la clase `CodonTransformer`, que transforma secuencias de ADN en codones.

   - **`protein_transformer.py`**: Define la clase `ProteinTransformer`, que transforma secuencias de codones en proteínas.

## Requisitos

- Python 3.x
- Biblioteca Biopython (`biopython`)
- Biblioteca VPython (`vpython`)
- Biblioteca pandas para el manejo de dataframes

## Instalación

1. Clona el repositorio o descarga el proyecto en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Instala las bibliotecas requeridas:

   ```bash
   pip install biopython vpython pandas
