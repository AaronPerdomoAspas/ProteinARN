from orchestator.DatabaseSaver import DatabaseSaver
from orchestator.FastaProcessor import FastaProcessor
from orchestator.ReplicationProcessor import ReplicationProcessor


class UnifiedOrchestrator:

    def __init__(self):
        self.fasta_processor = FastaProcessor()
        self.replication_processor = ReplicationProcessor()
        self.database_saver = DatabaseSaver()

    def download_fasta_files(self):
        """Descarga los archivos FASTA desde la API y los guarda en el directorio correspondiente"""
        print("Descargando archivos FASTA desde la API...")
        self.fasta_processor.download_fasta_files()

    def process_fasta_files(self):
        """Procesa todos los archivos FASTA y guarda los resultados en la base de datos"""
        fasta_files = self.fasta_processor.get_fasta_files()

        for fasta_file in fasta_files:
            result = self.replication_processor.process_file(fasta_file)
            if result:
                df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion = result
                self.database_saver.save_to_database(df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion)
