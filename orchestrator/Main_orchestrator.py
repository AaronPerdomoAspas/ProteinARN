import json
from typing import List, Optional

from conections.Connection import NCBIConnection
from downloader.FastaDownloader import FastaDownloader
from downloader.IdFetcher import IdFetcher
from downloader.SingleFastaDownloader import SingleFastaDownloader
from utils.FilePathHelper import FilePathHelper
from validator.FormatValidator import FormatValidator
from validator.NonEmptyValidator import NonEmptyValidator
from validator.SequenceValidator import SequenceValidator


class MainOrchestrator:
    def __init__(self, config: json):
        # Configuración del correo electrónico
        self.connection = NCBIConnection(config["email"]["address"])

        # Configuración de búsqueda de datos
        self.id_fetcher = IdFetcher(config)

        # Configuración de descarga
        self.single_fasta_downloader = SingleFastaDownloader(config["download"])
        self.downloader = FastaDownloader(self.single_fasta_downloader)

        # Configuración de validación
        self.validators = [
            FormatValidator(),
            SequenceValidator(),
            NonEmptyValidator()
        ]

    def execute(self, count: Optional[int] = None, ids: Optional[List[str]] = None) -> List[str]:
        self.connection.connect()

        identifiers = self._get_identifiers(count, ids)

        downloaded_files = self.downloader.download_fasta_files(identifiers)

        valid_files = self.validate_files(downloaded_files)

        print("\nArchivos FASTA válidos:", valid_files)
        return valid_files

    def validate_files(self, files: List[str]) -> List[str]:
        valid_files: List[str] = []
        for file_name in files:
            if file_name and all(validator.validate(file_name) for validator in self.validators):
                # Usar la función oculta para obtener solo el nombre del archivo
                valid_files.append(FilePathHelper.get_filename_only(file_name))
        return valid_files

    def _get_identifiers(self, count: Optional[int], ids: Optional[List[str]]) -> List[str]:
        return ids or (self.id_fetcher.fetch_ids(count) if count is not None else self._raise_missing_argument_error())

    def _raise_missing_argument_error(self) -> None:
        raise ValueError("Debe proporcionar 'count' o 'ids' para ejecutar el proceso.")
