# BIO Práctica Aula

Este proyecto es una práctica orientada a la gestión de bases de datos y la transformación de datos en un entorno académico. Está diseñado para ayudar a los estudiantes a comprender cómo interactuar con bases de datos mediante Python, automatizando tareas comunes como la creación, conexión, manipulación y transformación de datos. El proyecto se centra en la construcción de scripts modulares que permiten llevar a cabo estas operaciones de forma eficiente.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
  - [Requisitos Previos](#requisitos-previos)
  - [Pasos de Instalación](#pasos-de-instalación)
- [Uso](#uso)
  - [Conexión a la Base de Datos](#conexión-a-la-base-de-datos)
  - [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Descripción Detallada de los Módulos](#descripción-detallada-de-los-módulos)
  - [load/](#load)
  - [Transform/](#transform)

## Estructura del Proyecto

El proyecto está organizado en varios módulos, cada uno dedicado a un aspecto específico de la funcionalidad de la aplicación.


### Descripción General de los Directorios

- **load/**: Contiene los módulos encargados de la conexión y manipulación de la base de datos.
    - BBDD_Create.py: Este script se encarga de crear las tablas y las estructuras necesarias dentro de la base de datos.
    - BBDD_management.py: Maneja las operaciones de gestión sobre las tablas de la base de datos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en las tablas una vez que han sido creadas.
    - Connection.py: Contiene la lógica de conexión a la base de datos. Configura el host, el puerto, el usuario y la contraseña necesarios para establecer la conexión.
- **Transform/**: Incluye scripts para realizar transformaciones específicas en las columnas y datos de la base de datos.
    - columnas.py: Permite realizar operaciones sobre las columnas de las tablas. Puedes añadir nuevas columnas, cambiar el tipo de datos de las columnas existentes o eliminar columnas que ya no sean necesarias.
    - transform.py: Ejecuta transformaciones sobre los datos. Por ejemplo, puedes aplicar reglas de normalización o agregar nuevas derivadas a partir de las columnas existentes.
- **Main.py**: El archivo principal que coordina la ejecución de los diferentes módulos para llevar a cabo las operaciones necesarias.

### Requisitos Previos

- Python 3.x (Recomendado Python 3.7 o superior)
- Virtualenv (opcional pero recomendado para aislar las dependencias)
- Un sistema de gestión de bases de datos como MySQL o SQLite


