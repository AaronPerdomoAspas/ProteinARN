from pathlib import Path
from Bio import SeqIO


class FileManager:

    @staticmethod
    def get_fasta_files(directory: Path):
        """Obtiene todos los archivos FASTA del directorio especificado."""
        return list(directory.glob("*.fasta"))

    @staticmethod
    def read_fasta(fasta_file: Path):
        """Lee un archivo FASTA y retorna la secuencia de ADN."""
        sequences = []
        with open(fasta_file, "r") as file:
            for record in SeqIO.parse(file, "fasta"):
                sequences.append(str(record.seq))
        if not sequences:
            raise ValueError(f"No se encontró ninguna secuencia en el archivo {fasta_file}")
        return sequences[0]  # Si hay varias secuencias, devuelve la primera.
