class ProteinTransformer:
    @staticmethod
    def transform(codones):
        """
        Simula la transformación de una secuencia de codones a una lista de proteínas.
        """
        return [f"Aminoacido_{i}" for i, _ in enumerate(codones, 1)]
