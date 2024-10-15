from adn_replication.manager.FileManager import FileManager
from adn_replication.replicator.ConservativeReplicator import ConservativeReplicator
from adn_replication.replicator.DispersiveReplicator import DispersiveReplicator
from adn_replication.replicator.SemiconservativeReplicator import SemiconservativeReplicator


class ReplicationManager:
    @staticmethod
    def perform_all_replications(fasta_file):
        # Leer la secuencia original desde el archivo FASTA
        adn_original = FileManager.read_fasta(fasta_file)

        # Ejecutar replicación conservativa
        conservativa_replicator = ConservativeReplicator(adn_original)
        adn_conservativa = conservativa_replicator.replicate()

        # Ejecutar replicación semiconservativa
        semiconservativa_replicator = SemiconservativeReplicator(adn_original)
        adn_semiconservativa = semiconservativa_replicator.replicate()

        # Ejecutar replicación dispersiva
        dispersiva_replicator = DispersiveReplicator(adn_original)
        adn_dispersiva = dispersiva_replicator.replicate()

        return adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva
