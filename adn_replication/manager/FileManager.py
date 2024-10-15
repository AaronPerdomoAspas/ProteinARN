from Bio import SeqIO

class FileManager:
    @staticmethod
    def get_fasta_files(directory):
        """Obtiene una lista de todos los archivos FASTA en el directorio dado."""
        return list(directory.glob("*.fasta"))

    @staticmethod
    def read_fasta(fasta_file):
        """Lee una secuencia de ADN desde un archivo FASTA."""
        try:
            # Lee el archivo FASTA y devuelve la secuencia como una cadena.
            record = next(SeqIO.parse(str(fasta_file), "fasta"))
            return str(record.seq)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo {fasta_file}: {e}")
