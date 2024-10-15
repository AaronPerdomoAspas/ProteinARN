from pathlib import Path

from Bio import SeqIO

class FileManager:
    @staticmethod
    def get_fasta_files(directory):
        """Obtiene una lista de todos los archivos FASTA en el directorio dado."""
        directory = Path(directory)
        print(type(directory))
        return [f for f in directory.iterdir() if f.is_file() and f.suffix == '.fasta']


    @staticmethod
    def read_fasta(fasta_file):
        """Lee una secuencia de ADN desde un archivo FASTA."""
        try:
            # Lee el archivo FASTA y devuelve la secuencia como una cadena.
            record = next(SeqIO.parse(str(fasta_file), "fasta"))
            return str(record.seq)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo {fasta_file}: {e}")
