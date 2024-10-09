# Transformación y conexión con la base de datos:

Este proyecto es una práctica orientada a la gestión de bases de datos y la transformación de datos en un entorno académico. Está diseñado para ayudar a los estudiantes a comprender cómo interactuar con bases de datos mediante Python, automatizando tareas comunes como la creación, conexión, manipulación y transformación de datos. El proyecto se centra en la construcción de scripts modulares que permiten llevar a cabo estas operaciones de forma eficiente.

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
  - [Requisitos Previos](#requisitos-previos)
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

# ¿Por qué usar MySQL en lugar de MongoDB?

## Ventajas de MySQL frente a MongoDB

### Estructura Relacional
MySQL sigue un modelo de base de datos relacional, lo que lo convierte en la mejor opción para aplicaciones con datos altamente estructurados y donde las relaciones entre tablas son importantes.

### Transacciones ACID
MySQL soporta transacciones que cumplen con las propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad). Esto asegura que las operaciones sean fiables, especialmente en aplicaciones críticas como sistemas bancarios o que manejen información sensible.

### Lenguaje SQL y Herramientas Maduras
MySQL utiliza SQL, un lenguaje estándar muy extendido que tiene soporte en múltiples herramientas de desarrollo y administración de bases de datos. Esto permite integrar fácilmente MySQL con muchas tecnologías y frameworks.

### Integridad de Datos
Con soporte para claves foráneas, MySQL garantiza la integridad referencial entre tablas, asegurando que los datos estén correctamente relacionados y no haya inconsistencias.

### Consultas Complejas
MySQL permite realizar consultas avanzadas y optimizadas, incluyendo uniones (JOINs), subconsultas y agregaciones complejas, que son esenciales para aplicaciones que requieren manejar relaciones entre múltiples conjuntos de datos.

### Escalabilidad Vertical
MySQL puede mejorar su rendimiento simplemente añadiendo más recursos al servidor (memoria, CPU, etc.), lo que puede ser más eficiente para ciertos proyectos antes de considerar una infraestructura distribuida.

### Soporte para Procedimientos Almacenados
Permite ejecutar lógica de negocio directamente en la base de datos mediante procedimientos almacenados y triggers, lo que puede mejorar el rendimiento y simplificar las operaciones.

### Madurez y Comunidad
MySQL es una tecnología madura con décadas de desarrollo, lo que significa que tiene una comunidad grande, un ecosistema sólido de plugins y herramientas, así como buena documentación.

## Cuándo elegir MySQL sobre MongoDB

- Si los datos son altamente estructurados y las relaciones son importantes.
- Si tu aplicación requiere transacciones consistentes y confiables.
- Si necesitas realizar consultas complejas con relaciones múltiples.
- Si deseas aprovechar la madurez y estabilidad de una base de datos relacional.

## Conclusión
MySQL es una opción ideal para aplicaciones que requieren un esquema rígido, integridad referencial y soporte para transacciones robustas. En comparación, MongoDB es más adecuado para datos no estructurados o aplicaciones con escalabilidad horizontal masiva, pero no proporciona el mismo nivel de control relacional y transaccional que MySQL.




