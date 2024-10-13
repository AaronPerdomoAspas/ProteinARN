import pandas as pd

class TableWriter:
    @staticmethod
    def create_and_print_tables(adn_original, adn_conservativa, adn_semiconservativa, adn_dispersiva, codones, proteinas):
        data = {
            # Tabla Organismos (estos datos deben ser ajustados según cada organismo)
            "id_organismo": [12, 23, 34],
            "nombre": ["Escherichia coli", "Homo sapiens", "Saccharomyces cerevisiae"],
            "tipo": ["Bacteria", "Eucariota", "Levadura"],

            # Tabla ARNm
            "id_arnm": [101, 102, 103],
            "secuencia": ["AUGGCUAAGCUA", "AUGGCCGGAUCA", "AUGAAAGGCUAC"],
            "id_organismo": [12, 23, 34],

            # Tabla Codones
            "id_codon": [1001, 1002, 1003],
            "secuencia_codon": ["AUG", "GCU", "AAG"],
            "aminoacido": ["Metionina", "Alanina", "Lisina"],
            "id_arnm": [101, 101, 102],

            # Tabla Proteínas
            "id_proteina": [10001, 10002, 10003],
            "nombre": ["Proteína X", "Proteína Y", "Proteína Z"],
            "secuencia_aminoacidos": ["Met-Ala-Lis", "Met-Gly-His", "Ala-Lis-Glu"],
            "id_arnm": [101, 102, 103],

            # Tabla Clasificación de Proteínas
            "id_clasificacion": [5001, 5002, 5003],
            "nombre_clasificacion": ["Enzima", "Receptor", "Transportadora"],
            "id_proteina": [10001, 10002, 10003]
        }

        # Convertir el diccionario en un DataFrame de pandas
        df = pd.DataFrame(data)
        print(df)
