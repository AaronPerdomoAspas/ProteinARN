class CodonTransformer:
    @staticmethod
    def transform(adn_replicado):
        """
        Divide la secuencia replicada en codones (tripletes de bases).
        """
        return [adn_replicado[i:i+3] for i in range(0, len(adn_replicado), 3) if len(adn_replicado[i:i+3]) == 3]
