from Bio import Entrez
from typing import Optional
import os

class SingleFastaDownloader:
    def __init__(self, db: str, rettype: str, retmode: str, download_directory: str):
        self.db = db
        self.rettype = rettype
        self.retmode = retmode
        self.download_directory = download_directory
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def download(self, identifier: str) -> Optional[str]:
        """Descargar un archivo FASTA dado un identificador y devolver su nombre completo."""
        try:
            file_name = f"{identifier}.fasta"
            full_path = os.path.join(self.download_directory, file_name)
            with Entrez.efetch(db=self.db, id=identifier, rettype=self.rettype, retmode=self.retmode) as handle:
                with open(full_path, "w") as output:
                    output.write(handle.read())
            print(f"Archivo {file_name} descargado correctamente en {self.download_directory}.")
            return full_path
        except Exception as e:
            print(f"Ocurrió un error al descargar {identifier}: {e}")
            return None
