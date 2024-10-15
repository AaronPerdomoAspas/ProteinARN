import os
from pathlib import Path
from api_connection_download.orchestrator.Main_orchestrator import MainOrchestrator
from api_connection_download.config.Config import Config
from adn_replication.manager.FileManager import FileManager

class FastaProcessor:

    def __init__(self):
        self.fasta_directory = self._get_fasta_directory()

    def _get_fasta_directory(self):
        """Devuelve el directorio donde se guardan los archivos FASTA"""
        return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "api_connection_download", "download_fasta"))

    def download_fasta_files(self):
        """Llama al orquestador de la API para descargar los archivos FASTA"""
        orchestrator = MainOrchestrator(Config)
        ids = Config.get('data').get('ids')
        orchestrator.execute(ids=ids)

    def get_fasta_files(self):
        """Obtiene los archivos FASTA del directorio"""
        return FileManager.get_fasta_files(self.fasta_directory)
