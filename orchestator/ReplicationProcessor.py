import pandas as pd
from adn_replication.manager.ReplicationManager import ReplicationManager
from adn_replication.manager.TransformManager import TransformManager
from adn_replication.manager.VisualizationManager import VisualizationManager
from adn_replication.writer.DataframeWriter import DataFrameWriter


class ReplicationProcessor:

    def process_file(self, fasta_file):
        """Procesa un archivo FASTA, realizando las replicaciones y creando DataFrames"""
        print(f"Procesando el archivo FASTA: {fasta_file}")
        try:
            adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva = self._replicate_dna(fasta_file)

            codones, proteinas = self._transform_to_codons_and_proteins(adn_conservativa)

            df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion = self._create_dataframes(
                adn_conservativa, adn_semiconservativa, adn_dispersiva, codones, proteinas)

            self._visualize_replication(adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva)

            return df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion

        except Exception as e:
            print(f"Error durante el procesamiento del archivo {fasta_file}: {e}")
            return None

    def _replicate_dna(self, fasta_file):
        """Realiza las replicaciones del ADN a partir de un archivo FASTA"""
        return ReplicationManager.perform_all_replications(fasta_file)

    def _transform_to_codons_and_proteins(self, adn_conservativa):
        """Transforma la replicación conservativa en codones y proteínas"""
        return TransformManager.transform_adn(adn_conservativa)

    def _create_dataframes(self, adn_conservativa, adn_semiconservativa, adn_dispersiva, codones, proteinas):
        """Crea los DataFrames necesarios a partir de las replicaciones y las transformaciones"""
        df_organismos = DataFrameWriter.create_organisms_table()
        df_arnm_conservativa = DataFrameWriter.create_arnm_table(adn_conservativa, 'conservativa')
        df_arnm_semiconservativa = DataFrameWriter.create_arnm_table(adn_semiconservativa, 'semiconservativa')
        df_arnm_dispersiva = DataFrameWriter.create_arnm_table(adn_dispersiva, 'dispersiva')
        df_codones = DataFrameWriter.create_codons_table(codones)
        df_proteinas = DataFrameWriter.create_proteins_table(proteinas)
        df_clasificacion = DataFrameWriter.create_classification_table(['Clasificación 1', 'Clasificación 2'])

        df_arnm = pd.concat([df_arnm_conservativa, df_arnm_semiconservativa, df_arnm_dispersiva], ignore_index=True)

        return df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion

    def _visualize_replication(self, adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva):
        """Genera las representaciones gráficas en 3D de las replicaciones"""
        VisualizationManager.representar_proceso_3d(adn_original, adn_conservativa)
        VisualizationManager.representar_proceso_3d(adn_original, adn_semiconservativa)
        VisualizationManager.representar_proceso_3d(adn_original, adn_dispersiva)
