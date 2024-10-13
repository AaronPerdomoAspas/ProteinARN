class DispersiveReplicator:
    def __init__(self, adn_original):
        self.adn_original = adn_original

    def replicate(self):
        """
        Simula la replicación dispersiva del ADN, en la cual se obtiene una
        molécula de ADN con fragmentos de la cadena original y fragmentos de la cadena nueva.
        """
        # En la replicación dispersiva, las cadenas se mezclan en fragmentos.
        adn_replicated = ''.join(
            self.adn_original[i] if i % 2 == 0 else 'N'  # 'N' simula un fragmento nuevo
            for i in range(len(self.adn_original))
        )
        return adn_replicated
