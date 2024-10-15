import pandas as pd
from adn_replication.manager.FileManager import FileManager
from adn_replication.manager.ReplicationManager import ReplicationManager
from adn_replication.manager.TransformManager import TransformManager
from adn_replication.manager.VisualizationManager import VisualizationManager
from adn_replication.writer.DataframeWriter import *
from pathlib import Path

from adn_replication.writer.DataframeWriter import DataFrameWriter


def main():
    # Definir la ruta relativa desde el archivo main.py
    fasta_directory = Path(__file__).resolve().parent.parent / "api_connection_download" / "download_fasta"

    # Obtener los archivos FASTA disponibles
    fasta_files = FileManager.get_fasta_files(fasta_directory)

    # Procesar cada archivo FASTA
    for fasta_file in fasta_files:
        print(f"Procesando el archivo FASTA: {fasta_file}")

        try:
            # Realizar las tres replicaciones del ADN
            adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva = ReplicationManager.perform_all_replications(
                fasta_file)

            # Transformar el ADN replicado en codones y proteínas (usando la replicación conservativa como base)
            codones, proteinas = TransformManager.transform_adn(adn_conservativa)

            # Crear los dataframes
            df_organismos = DataFrameWriter.create_organisms_table()
            df_arnm_conservativa = DataFrameWriter.create_arnm_table(adn_conservativa, 'conservativa')
            df_arnm_semiconservativa = DataFrameWriter.create_arnm_table(adn_semiconservativa, 'semiconservativa')
            df_arnm_dispersiva = DataFrameWriter.create_arnm_table(adn_dispersiva, 'dispersiva')
            df_codones = DataFrameWriter.create_codons_table(codones)
            df_proteinas = DataFrameWriter.create_proteins_table(proteinas)
            df_clasificacion = DataFrameWriter.create_classification_table(['Clasificación 1', 'Clasificación 2'])

            # Combinar los tres DataFrames de ARNm en uno solo
            df_arnm = pd.concat([df_arnm_conservativa, df_arnm_semiconservativa, df_arnm_dispersiva], ignore_index=True)
            df_arnm['id_arnm'] = range(1, len(df_arnm) + 1)

            # Representación gráfica del proceso de replicación en 3D para cada replicación
            VisualizationManager.representar_proceso_3d(adn_original, adn_conservativa)
            VisualizationManager.representar_proceso_3d(adn_original, adn_semiconservativa)
            VisualizationManager.representar_proceso_3d(adn_original, adn_dispersiva)

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error durante el procesamiento del archivo {fasta_file}: {e}")


if __name__ == "__main__":
    main()
