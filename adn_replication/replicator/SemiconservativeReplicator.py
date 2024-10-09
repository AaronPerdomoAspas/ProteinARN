class SemiconservativeReplicator:
    @staticmethod
    def replicate(adn):
        """
        Simula el proceso de replicación del ADN siguiendo el modelo semiconservativo.
        """
        adn_replicado = ""
        for base in adn:
            # Copiar la hebra original
            adn_replicado += base
        return adn_replicado  # Se mantiene igual porque la hebra replicada tiene mitad original y mitad copiada
