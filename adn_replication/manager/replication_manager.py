from adn_replication.reader.fasta_reader import FastaReader
from adn_replication.replicator.conservative_replicator import ConservativeReplicator
from adn_replication.replicator.dispersive_replicator import DispersiveReplicator
from adn_replication.replicator.semiconservative_replicator import SemiconservativeReplicator


class ReplicationManager:
    @staticmethod
    def perform_replication(fasta_file):
        adn_original = FastaReader.read(fasta_file)

        # Seleccionar el tipo de replicación a realizar
        print("Seleccione el modelo de replicación:")
        print("1. Conservativa")
        print("2. Semiconservativa")
        print("3. Dispersiva")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            return ConservativeReplicator.replicate(adn_original), adn_original
        elif opcion == "2":
            return SemiconservativeReplicator.replicate(adn_original), adn_original
        elif opcion == "3":
            return DispersiveReplicator.replicate(adn_original), adn_original
        else:
            raise ValueError("Opción no válida. Saliendo del programa.")
