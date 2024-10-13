class SemiconservativeReplicator:
    def __init__(self, adn_original):
        self.adn_original = adn_original

    def replicate(self):
        """
        Simula la replicación semiconservativa del ADN, en la cual se obtiene una
        molécula de ADN con una cadena original y una cadena nueva.
        """
        # En la replicación semiconservativa, una cadena original se empareja
        # con una cadena nueva.
        adn_replicated = self.adn_original[::-1]  # Representa la cadena nueva replicada.
        return adn_replicated
