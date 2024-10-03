
from typing import List

from config.Config import Config
from downloader.Connection import NCBIConnection
from downloader.FastaDownloader import FastaDownloader
from downloader.SingleFastaDownloader import SingleFastaDownloader
from validator.FormatValidator import FormatValidator
from validator.NonEmptyValidator import NonEmptyValidator
from validator.SequenceValidator import SequenceValidator


class MainOrchestrator:
    def __init__(self, config: Config):
        self.config = config
        self.connection = NCBIConnection(self.config["email"])
        self.validators = [
            FormatValidator(),
            SequenceValidator(),
            NonEmptyValidator()
        ]

    def execute(self) -> List[str]:
        # Conectar a la API
        self.connection.connect()

        # Inicializar la clase de descarga
        single_fasta_downloader = SingleFastaDownloader(
            self.config["db"],
            self.config["rettype"],
            self.config["retmode"],
            self.config["download_directory"]
        )
        downloader = FastaDownloader(single_fasta_downloader)

        # Lista de identificadores para descargar
        ids = ["NM_001301717", "NM_001374413", "NM_001301720"]

        # Descargar los archivos FASTA
        downloaded_files = downloader.download_fasta_files(ids)

        # Validar los archivos descargados
        valid_files: List[str] = []
        for file_name in downloaded_files:
            if file_name and all(validator.validate(file_name) for validator in self.validators):
                valid_files.append(file_name)

        # Imprimir los archivos válidos
        print("Archivos FASTA válidos:", valid_files)
        return valid_files
