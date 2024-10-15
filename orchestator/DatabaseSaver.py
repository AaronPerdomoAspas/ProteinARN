from load_result.load.BBDD_Create import crear_tablas
from load_result.load.BBDD_management import insert_data
from load_result.load.Connection import connection


class DatabaseSaver:

    def save_to_database(self, df_organismos, df_arnm, df_codones, df_proteinas, df_clasificacion):
        """Guarda los DataFrames en la base de datos"""
        conn, cursor = connection()
        crear_tablas(conn, cursor)
        insert_data(df_organismos, "organismos", df_organismos)
        insert_data(df_arnm, "arnm", df_arnm)
        insert_data(df_codones, "codones", df_codones)
        insert_data(df_proteinas, "proteinas", df_proteinas)
        insert_data(df_clasificacion, "clasificacion_proteinas", df_clasificacion)
        conn.close()
