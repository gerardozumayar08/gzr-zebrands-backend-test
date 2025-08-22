import traceback


def get_exception_details(exc):
    tipo_excepcion = type(exc).__name__
    valor_excepcion = str(exc)
    traceback_info = traceback.format_exc()
    tb = exc.__traceback__
    detalles_excepcion = {
        "tipo_excepcion": tipo_excepcion,
        "valor_excepcion": valor_excepcion,
        "archivo": None,
        "numero_linea": None,
        "codigo_en_linea": None,
        "traza_completa": None,
    }
    if tb:
        file_name = tb.tb_frame.f_code.co_filename
        line_number = tb.tb_lineno
        line_code = open(file_name).readlines()[line_number - 1].strip()
        detalles_excepcion = {
            "tipo_excepcion": tipo_excepcion,
            "valor_excepcion": valor_excepcion,
            "archivo": file_name,
            "numero_linea": line_number,
            "codigo_en_linea": line_code,
            "traza_completa": traceback_info,
        }
    return detalles_excepcion
