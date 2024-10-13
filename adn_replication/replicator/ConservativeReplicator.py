class ConservativeReplicator:
    def __init__(self, adn_original):
        self.adn_original = adn_original

    def replicate(self):
        """
        Simula la replicación conservativa del ADN, en la cual se obtiene una
        molécula de ADN nueva idéntica y una molécula completamente original.
        """
        # En la replicación conservativa, se mantiene una cadena original y se
        # produce una nueva idéntica a la original.
        adn_replicated = self.adn_original  # Representa la cadena nueva replicada.
        return adn_replicated
