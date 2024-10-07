from pathlib import Path


class FileManager:
    @staticmethod
    def get_fasta_files(directory):
        fasta_directory = Path(directory)
        fasta_files = list(fasta_directory.glob("*.fasta"))

        if not fasta_files:
            raise FileNotFoundError("No se encontraron archivos FASTA en la ruta especificada.")

        print("Archivos FASTA encontrados:")
        for fasta_file in fasta_files:
            print(f"- {fasta_file}")

        return fasta_files
