from load_result.load.Connection import connection


def insert_data(df, table_name, columns):
    conn, cursor = connection()
    # Generar la cadena de nombres de columnas para SQL
    cols_table = ",".join(list(columns.values()))
    # Generar el formato de placeholders para los valores de la consulta SQL (%s, %s, ...)
    valores_format = ("%s," * len(columns))[:-1]
    rows_multiple = []
    for i, row in df.iterrows():
        rows_multiple.append(tuple(row))
    sql = (f"INSERT INTO {table_name}" + " (" + cols_table + ") VALUES (" + valores_format + ")")
    # Insertamos en la base de datos muchos registros a la vez
    cursor.executemany(sql, rows_multiple)
    conn.commit()
    conn.close()