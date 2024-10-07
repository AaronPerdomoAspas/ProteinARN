from load.Connection import connection


def insert_data(df, cols_table, valores_format, table_name):
    conn, cursor = connection()
    rows_multiple = []
    for i, row in df.iterrows():
        rows_multiple.append(tuple(row))
    sql = (f"INSERT INTO {table_name}" + " (" + cols_table + ") VALUES (" + valores_format + ")")
    # Insertamos en la base de datos muchos registros a la vez
    cursor.executemany(sql, rows_multiple)
    conn.commit()
    conn.close()