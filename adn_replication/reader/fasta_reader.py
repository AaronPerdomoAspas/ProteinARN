from Bio import SeqIO

class FastaReader:
    @staticmethod
    def read(fasta_file):
        """
        Lee un archivo FASTA y devuelve la secuencia de ADN.
        """
        for record in SeqIO.parse(str(fasta_file), "fasta"):
            return str(record.seq)
