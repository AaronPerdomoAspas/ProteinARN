import logging


def transform(df, columns):
    """
    Transforma el DataFrame seleccionando solo las columnas que coinciden con el mapeo de 'columns'.
    Genera también las cadenas para la consulta SQL (nombres de columnas y placeholders de valores).

    Args:
    df (DataFrame): El DataFrame que contiene los datos a transformar.
    columns (dict): Un diccionario que mapea las columnas del DataFrame a las columnas de la base de datos.

    Returns:
    df (DataFrame): El DataFrame filtrado con las columnas especificadas.
    cols_table (str): Una cadena con los nombres de las columnas para SQL.
    valores_format (str): Una cadena con el formato de valores (%s, %s, ...) para SQL.
    """
    try:
        # Seleccionar solo las columnas relevantes según el mapeo
        df = df[list(columns.keys())].copy()

        # Generar la cadena de nombres de columnas para SQL
        cols_table = ",".join(list(columns.values()))

        # Generar el formato de placeholders para los valores de la consulta SQL (%s, %s, ...)
        valores_format = ("%s," * len(columns))[:-1]  # Crear tantos %s como columnas, eliminando la última coma

        return df, cols_table, valores_format

    except Exception as err:
        logging.error("Error al crear el dataframe \n")
        logging.error(err)
        return None, None, None
