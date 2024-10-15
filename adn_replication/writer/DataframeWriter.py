import pandas as pd


class DataFrameWriter:
    @staticmethod
    def create_organisms_table():
        """
        Crea un dataframe de la tabla Organismos.
        """
        data_organismos = {
            'id_organismo': [1],
            'nombre': ['Organismo Simulado'],
            'tipo': ['Eucariota']
        }

        df_organismos = pd.DataFrame(data_organismos)
        return df_organismos

    @staticmethod
    def create_arnm_table(adn_replicado, metodo_replicacion):
        """
        Crea un dataframe de la tabla ARNm usando la secuencia de ADN replicado.
        """
        data_arnm = {
            'id_arnm': [1],
            'secuencia': [adn_replicado],
            'id_organismo': [1],
            'metodo_replicacion': [metodo_replicacion],
        }

        df_arnm = pd.DataFrame(data_arnm)
        return df_arnm

    @staticmethod
    def create_codons_table(codones):
        """
        Crea un dataframe de la tabla Codones usando la lista de codones.
        """
        data_codones = {
            'id_codon': list(range(1, len(codones) + 1)),
            'secuencia_codon': codones,
            'aminoacido': [f"Aminoacido_{i}" for i in range(1, len(codones) + 1)],
            'id_arnm': [1] * len(codones)
        }

        df_codones = pd.DataFrame(data_codones)
        return df_codones

    @staticmethod
    def create_proteins_table(proteinas):
        """
        Crea un dataframe de la tabla Proteínas usando la lista de proteínas.
        """
        data_proteinas = {
            'id_proteina': [1],
            'nombre': ['Proteina Simulada'],
            'secuencia_aminoacidos': ['-'.join(proteinas)],
            'id_arnm': [1]
        }

        df_proteinas = pd.DataFrame(data_proteinas)
        return df_proteinas

    @staticmethod
    def create_classification_table(clasificaciones):
        """
        Crea un dataframe de la tabla Clasificación de Proteínas usando las clasificaciones.
        """
        data_clasificacion = {
            'id_clasificacion': list(range(1, len(clasificaciones) + 1)),
            'nombre_clasificacion': clasificaciones,
            'id_proteina': [1] * len(clasificaciones)
        }

        df_clasificacion = pd.DataFrame(data_clasificacion)
        return df_clasificacion
