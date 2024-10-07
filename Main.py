from load.Connection import connection
from Transform.transform import transform
from Transform.columnas import organismo
from Transform.columnas import arm
from Transform.columnas import codones
from Transform.columnas import proteinas
from Transform.columnas import clasificacion
from load.BBDD_Create import crear_tablas
from load.BBDD_management import insert_data
import pandas as pd



# Mostrar el DataFrame

if __name__ == '__main__':
    conn, cursor = connection()
    # Datos de ejemplo --> ficticios
    data = {
        # Tabla Organismos
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

        # Tabla Proteinas
        "id_proteina": [10001, 10002, 10003],
        "nombre": ["Proteína X", "Proteína Y", "Proteína Z"],
        "secuencia_aminoacidos": ["Met-Ala-Lis", "Met-Gly-His", "Ala-Lis-Glu"],
        "id_arnm": [101, 102, 103],

        # Tabla Clasificacion_Proteinas
        "id_clasificacion": [5001, 5002, 5003],
        "nombre_clasificacion": ["Enzima", "Receptor", "Transportadora"],
        "id_proteina": [10001, 10002, 10003]
    }
    # Crear un DataFrame ficticio con todas las columnas de las tablas

    # Crear el DataFrame
    df = pd.DataFrame(data)
    df_organismo, cols_table_organismo, valores_format_organismo = transform(df, organismo)
    df_arm, cols_table_arm, valores_format_arm = transform(df, arm)
    df_codones, cols_table_codones, valores_format_codones = transform(df, codones)
    df_proteinas, cols_table_proteinas, valores_format_proteinas = transform(df, proteinas)
    df_clasificacion, cols_table_clasificacion, valores_format_clasificacion = transform(df, clasificacion)
    crear_tablas(conn, cursor)
    insert_data(df_organismo, cols_table_organismo, valores_format_organismo, "organismos")
    insert_data(df_arm, cols_table_arm, valores_format_arm, "arnm")
    insert_data(df_codones, cols_table_codones, valores_format_codones, "codones")
    insert_data(df_proteinas, cols_table_proteinas, valores_format_proteinas, "proteinas")
    insert_data(df_clasificacion, cols_table_clasificacion, valores_format_clasificacion, "clasificacion_proteinas")
    a = 1