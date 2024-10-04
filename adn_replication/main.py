from pathlib import Path
from reader.fasta_reader import FastaReader
from replicator.conservative_replicator import ConservativeReplicator
from replicator.semiconservative_replicator import SemiconservativeReplicator
from replicator.dispersive_replicator import DispersiveReplicator
from transformer.codon_transformer import CodonTransformer
from transformer.protein_transformer import ProteinTransformer
from writer.dataframe_writer import DataFrameWriter
from vpython import cylinder, vector, color, rate, scene, text
import random

class ReplicacionADN:
    def __init__(self, secuencia_adn):
        self.secuencia_adn = secuencia_adn

    def ejecutar_replicacion(self):
        # Simulamos la replicación de la cadena de ADN
        cadena_lider = []
        cadena_rezagada = []
        for base in self.secuencia_adn:
            # Se agregan las bases en la cadena líder
            cadena_lider.append(base)
            # Se generan bases complementarias para la cadena rezagada
            cadena_rezagada.append(self.complementaria(base))
        return "".join(cadena_lider), "".join(cadena_rezagada)

    @staticmethod
    def complementaria(base):
        # Función para obtener la base complementaria
        complementos = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return complementos[base]


# Función para representar en 3D el proceso de replicación
def representar_proceso_3d(cadena_lider, cadena_rezagada):
    scene.title = "Replicación del ADN en 3D"
    scene.background = color.white

    # Colores para cada base
    color_base = {
        'A': color.red,  # Adenina
        'T': color.yellow,  # Timina
        'C': color.blue,  # Citosina
        'G': color.green  # Guanina
    }

    # Posiciones para la visualización
    for i, base in enumerate(cadena_lider):
        rate(2)  # Control de velocidad del proceso en tiempo real
        # Crear cilindros para la cadena líder
        cylinder(pos=vector(i, 1, 0), axis=vector(0, 1, 0), radius=0.1, color=color_base[base])
        # Crear etiquetas para la cadena líder
        text(pos=vector(i, 1, 0), text=base, color=color.black, height=0.2, depth=0.1)

    for i, base in enumerate(cadena_rezagada):
        rate(2)
        # Crear cilindros para la cadena rezagada
        cylinder(pos=vector(i, -1, 0), axis=vector(0, 1, 0), radius=0.1, color=color_base[base])
        # Crear etiquetas para la cadena rezagada
        text(pos=vector(i, -1, 0), text=base, color=color.black, height=0.2, depth=0.1)

    # Simular la adición de nuevas bases (representación simplificada)
    for i in range(len(cadena_lider)):
        rate(1)
        # Adición de una nueva base a la cadena líder
        base_nueva = random.choice(list(color_base.keys()))
        cylinder(pos=vector(i + len(cadena_lider), 1, 0), axis=vector(0, 1, 0), radius=0.1,
                 color=color_base[base_nueva])
        text(pos=vector(i + len(cadena_lider), 1, 0), text=base_nueva, color=color.black, height=0.2, depth=0.1)


def main(fasta_files):
    for fasta_file in fasta_files:
        print(f"Procesando el archivo FASTA: {fasta_file}")

        # Asegúrate de que se está pasando el archivo como string
        adn_original = FastaReader.read(fasta_file)

        # Seleccionar el tipo de replicación a realizar
        print("Seleccione el modelo de replicación:")
        print("1. Conservativa")
        print("2. Semiconservativa")
        print("3. Dispersiva")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            adn_replicado = ConservativeReplicator.replicate(adn_original)
        elif opcion == "2":
            adn_replicado = SemiconservativeReplicator.replicate(adn_original)
        elif opcion == "3":
            adn_replicado = DispersiveReplicator.replicate(adn_original)
        else:
            print("Opción no válida. Saliendo del programa.")
            return

        # Transformar la secuencia replicada en codones
        codones = CodonTransformer.transform(adn_replicado)

        # Transformar los codones en proteínas
        proteinas = ProteinTransformer.transform(codones)

        # Crear las tablas en dataframes
        tablas = DataFrameWriter.write(adn_original, adn_replicado, codones, proteinas, ['Clasificacion Simulada'])

        # Imprimir los dataframes
        for nombre_tabla, df in tablas.items():
            print(f"Tabla: {nombre_tabla}")
            print(df)
            print("\n")

        # Representación gráfica del proceso de replicación en 3D
        representar_proceso_3d(adn_original, adn_replicado)


if __name__ == "__main__":
    # Definir la ruta relativa desde el archivo main.py
    fasta_directory = Path(__file__).resolve().parent.parent / "api_connection_download" / "download_fasta"

    # Listar los archivos FASTA disponibles
    fasta_files = list(fasta_directory.glob("*.fasta"))

    # Comprobar que hay archivos FASTA en la carpeta
    if fasta_files:
        print("Archivos FASTA encontrados:")
        for fasta_file in fasta_files:
            print(f"- {fasta_file}")

        # Ejecutar la función principal con la lista de archivos FASTA
        main(fasta_files)
    else:
        raise FileNotFoundError("No se encontraron archivos FASTA en la ruta especificada.")
