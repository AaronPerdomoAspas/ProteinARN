import logging


def crear_tablas(connection_db, cursor):
    """
    Crea las tablas necesarias en la base de datos de bioinformática.
    Utiliza la conexión proporcionada por la función connection().
    Registra los errores con logging si hay problemas.
    """
    try:
        # Usamos tu función connection() para obtener la conexión y el cursor
        if connection_db and cursor:  # Verificamos que la conexión sea exitosa

            # Crear la tabla de Organismos
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Organismos (
                id_organismo INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                tipo VARCHAR(100)
            )
            """)

            # Crear la tabla de ARNm
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ARNm (
                id_arnm INT AUTO_INCREMENT PRIMARY KEY,
                secuencia TEXT NOT NULL,
                id_organismo INT,
                metodo_replicacion TEXT NOT NULL,
                FOREIGN KEY (id_organismo) REFERENCES Organismos(id_organismo)
            )
            """)

            # Crear la tabla de Codones
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Codones (
                id_codon INT AUTO_INCREMENT PRIMARY KEY,
                secuencia_codon CHAR(3) NOT NULL,
                aminoacido VARCHAR(50),
                id_arnm INT,
                FOREIGN KEY (id_arnm) REFERENCES ARNm(id_arnm)
            )
            """)

            # Crear la tabla de Proteínas
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Proteinas (
                id_proteina INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                secuencia_aminoacidos TEXT NOT NULL,
                id_arnm INT,
                FOREIGN KEY (id_arnm) REFERENCES ARNm(id_arnm)
            )
            """)

            # Crear la tabla de Clasificación de Proteínas
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clasificacion_Proteinas (
                id_clasificacion INT AUTO_INCREMENT PRIMARY KEY,
                nombre_clasificacion VARCHAR(255),
                id_proteina INT,
                FOREIGN KEY (id_proteina) REFERENCES Proteinas(id_proteina)
            )
            """)

            # Confirmar los cambios en la base de datos
            connection_db.commit()

            print("Tablas creadas exitosamente.")
        else:
            raise Exception("No se pudo establecer la conexión a la base de datos.")

    except Exception as e:
        # Registrar el error usando logging
        logging.error(f"Error durante la creación de tablas: {e}")
    finally:
        # Asegurarse de cerrar el cursor y la conexión si fueron inicializados correctamente
        if cursor != "":
            cursor.close()
        if connection_db != "":
            connection_db.close()