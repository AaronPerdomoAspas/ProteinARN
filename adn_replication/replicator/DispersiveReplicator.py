import random

class DispersiveReplicator:
    @staticmethod
    def replicate(adn):
        """
        Simula el proceso de replicación del ADN siguiendo el modelo dispersivo.
        Cada fragmento puede provenir de la hebra original o de la hebra replicada, de forma aleatoria.
        """
        adn_replicado = ""
        for base in adn:
            # Mezclamos fragmentos de la hebra original y replicada
            if random.choice([True, False]):
                adn_replicado += base
            else:
                adn_replicado += base.lower()  # Indicamos los fragmentos replicados como minúsculas para diferenciarlos
        return adn_replicado.upper()  # Convertimos todo a mayúsculas para estandarizar después
