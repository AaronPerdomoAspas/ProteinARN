from load_result.load.BBDD_Create import crear_tablas
from load_result.load.BBDD_management import insert_data
from load_result.load.Connection import connection

# Mostrar el DataFrame

if __name__ == '__main__':
    conn, cursor = connection()
    # Crear un DataFrame ficticio con todas las columnas de las tablas

    # Crear el DataFrame
    crear_tablas(conn, cursor)
    insert_data(df_organismo, "organismos", organismo)
    insert_data(df_arm, "arnm", arm)
    insert_data(df_codones, "codones", codones)
    insert_data(df_proteinas,"proteinas", proteinas)
    insert_data(df_clasificacion, "clasificacion_proteinas", clasificacion)