from Bio import SeqIO
from Bio.Seq import Seq

class SequenceValidator:
    @staticmethod
    def validate(file_name: str) -> bool:
        """Comprueba que las secuencias en el archivo sean válidas."""
        try:
            with open(file_name, "r") as file_handle:
                records = list(SeqIO.parse(file_handle, "fasta"))
                if all(isinstance(record.seq, Seq) for record in records):
                    print(f"{file_name} contiene secuencias válidas.")
                    return True
                else:
                    print(f"{file_name} contiene secuencias inválidas.")
                    return False
        except Exception as e:
            print(f"Error al validar las secuencias de {file_name}: {e}")
            return False
