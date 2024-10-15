from pathlib import Path

from adn_replication.manager.FileManager import FileManager
from api_connection_download.config.Config import Config
from api_connection_download.orchestrator.Main_orchestrator import MainOrchestrator
from adn_replication.manager.ReplicationManager import ReplicationManager
from adn_replication.manager.TransformManager import TransformManager
from adn_replication.manager.VisualizationManager import VisualizationManager
from adn_replication.writer.DataframeWriter import *

from load_result.columns.Columns import arm, organismo, codones_col, clasificacion, proteinas_col
from load_result.load.BBDD_Create import crear_tablas
from load_result.load.BBDD_management import insert_data
from load_result.load.Connection import connection


def main() -> None:
    orchestrator = MainOrchestrator(Config)
    count = Config.get('data').get('count')
    orchestrator.execute(count=count)

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

            conn, cursor = connection()

            crear_tablas(conn, cursor)
            insert_data(df_organismos, "organismos", organismo)
            insert_data(df_arnm, "arnm", arm)
            insert_data(df_codones, "codones", codones_col)
            insert_data(df_proteinas, "proteinas", proteinas_col)
            insert_data(df_clasificacion, "clasificacion_proteinas", clasificacion)
            print("insertado con exito")
            # Representación gráfica del proceso de replicación en 3D para cada replicación
            VisualizationManager.representar_proceso_3d(adn_original, adn_conservativa)
            VisualizationManager.representar_proceso_3d(adn_original, adn_semiconservativa)
            VisualizationManager.representar_proceso_3d(adn_original, adn_dispersiva)

        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
