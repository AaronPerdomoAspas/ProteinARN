from adn_replication.transformer.CodonTransformer import CodonTransformer
from adn_replication.transformer.ProteinTransformer import ProteinTransformer

class TransformManager:
    @staticmethod
    def transform_adn(adn_replicado):
        # Crear instancia del transformador de codones
        codon_transformer = CodonTransformer()
        codones = codon_transformer.transform(adn_replicado)

        # Crear instancia del transformador de proteínas
        protein_transformer = ProteinTransformer()
        proteinas = protein_transformer.transform(codones)

        return codones, proteinas
