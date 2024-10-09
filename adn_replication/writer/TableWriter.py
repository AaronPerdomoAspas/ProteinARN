from adn_replication.writer.DataframeWriter import DataFrameWriter


class TableWriter:
    @staticmethod
    def create_and_print_tables(adn_original, adn_replicado, codones, proteinas):
        tablas = DataFrameWriter.write(adn_original, adn_replicado, codones, proteinas, ['Clasificacion Simulada'])

        # Imprimir los dataframes
        for nombre_tabla, df in tablas.items():
            print(f"Tabla: {nombre_tabla}")
            print(df)
            print("\n")
