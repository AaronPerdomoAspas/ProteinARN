from manager.FileManager import FileManager
from manager.ReplicationManager import ReplicationManager
from manager.TransformManager import TransformManager
from manager.VisualizationManager import VisualizationManager
from writer.TableWriter import TableWriter
from pathlib import Path


def main():
    # Definir la ruta relativa desde el archivo main.py
    fasta_directory = Path(__file__).resolve().parent.parent / "api_connection_download" / "download_fasta"

    # Obtener los archivos FASTA disponibles
    fasta_files = FileManager.get_fasta_files(fasta_directory)

    # Procesar cada archivo FASTA
    for fasta_file in fasta_files:
        print(f"Procesando el archivo FASTA: {fasta_file}")

        try:
            # Realizar la replicación del ADN
            adn_replicado, adn_original = ReplicationManager.perform_replication(fasta_file)

            # Transformar el ADN replicado en codones y proteínas
            codones, proteinas = TransformManager.transform_adn(adn_replicado)

            # Crear e imprimir las tablas en dataframes
            TableWriter.create_and_print_tables(adn_original, adn_replicado, codones, proteinas)

            # Representación gráfica del proceso de replicación en 3D
            VisualizationManager.representar_proceso_3d(adn_original, adn_replicado)

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Error durante el procesamiento del archivo {fasta_file}: {e}")


if __name__ == "__main__":
    main()