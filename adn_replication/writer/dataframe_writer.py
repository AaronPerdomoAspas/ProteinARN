import pandas as pd

class DataFrameWriter:
    @staticmethod
    def write(adn_original, adn_replicado, codones, proteinas, clasificaciones):
        """
        Crea un dataframe simulando las tablas de la base de datos.
        """
        # Tabla Organismos
        data_organismos = {
            'id_organismo': [1],
            'nombre': ['Organismo Simulado'],
            'tipo': ['Eucariota']
        }
        df_organismos = pd.DataFrame(data_organismos)

        # Tabla ARNm
        data_arnm = {
            'id_arnm': [1],
            'secuencia': [adn_replicado],
            'id_organismo': [1]
        }
        df_arnm = pd.DataFrame(data_arnm)

        # Tabla Codones
        data_codones = {
            'id_codon': list(range(1, len(codones) + 1)),
            'secuencia_codon': codones,
            'aminoacido': [f"Aminoacido_{i}" for i in range(1, len(codones) + 1)],
            'id_arnm': [1] * len(codones)
        }
        df_codones = pd.DataFrame(data_codones)

        # Tabla Proteínas
        data_proteinas = {
            'id_proteina': [1],
            'nombre': ['Proteina Simulada'],
            'secuencia_aminoacidos': ['-'.join(proteinas)],
            'id_arnm': [1]
        }
        df_proteinas = pd.DataFrame(data_proteinas)

        # Tabla Clasificación de Proteínas
        data_clasificacion = {
            'id_clasificacion': [1],
            'nombre_clasificacion': clasificaciones,
            'id_proteina': [1]
        }
        df_clasificacion = pd.DataFrame(data_clasificacion)

        # Creación de un diccionario de dataframes para simular las tablas
        tablas = {
            'Organismos': df_organismos,
            'ARNm': df_arnm,
            'Codones': df_codones,
            'Proteinas': df_proteinas,
            'Clasificacion_Proteinas': df_clasificacion
        }

        return tablas
