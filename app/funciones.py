import math


def calcular_tasa_mensual_y_meses(tasainteres, periodo):
    """
    Convierte una tasa de interés anual a una tasa mensual y calcula el número total de meses.

    Args:
    - tasainteres (float): Tasa de interés anual en porcentaje (e.g., 5.0 para 5%).
    - periodo (int): Período en años.

    Returns:
    - tasamensual (float): Tasa mensual en formato decimal.
    - meses (int): Número total de meses en el período.
    """
    tasamensual = tasainteres / 100 / 12  # Convertir tasa anual a mensual en decimal
    meses = periodo * 12  # Convertir periodo en años a meses
    return tasamensual, meses


def generar_tabla(periodo, capital, tasamensual, aportemensual):
    """
    Genera una tabla con detalles financieros por año: inversión total, capital final y ganancia.

    Args:
    - periodo (int): Período en años.
    - capital (float): Capital inicial invertido.
    - tasamensual (float): Tasa mensual en formato decimal.
    - aportemensual (float): Aporte mensual constante.

    Returns:
    - datos_tabla (list): Lista de diccionarios, donde cada diccionario contiene:
        - 'Año' (int): Número del año.
        - 'Inversion_total' (float): Suma del capital inicial y los aportes realizados hasta ese año.
        - 'Capital_final' (float): Monto total acumulado al final del año.
        - 'Ganancia' (float): Ganancia obtenida al final del año.
    """
    datos_tabla = []
    for año in range(1, periodo + 1):
        meses_año = año * 12
        monto_año_capital = capital * math.pow(1 + tasamensual, meses_año)
        monto_año_aportes = aportemensual * ((math.pow(1 + tasamensual, meses_año) - 1) / tasamensual)
        total_año = round(monto_año_capital + monto_año_aportes, 2)
        inversion_año = capital + (aportemensual * meses_año)
        ganancia_año = round(total_año - inversion_año, 2)

        datos_tabla.append({
            'Año': año,
            'Inversion_total': round(inversion_año, 2),
            'Capital_final': total_año,
            'Ganancia': ganancia_año
        })
    return datos_tabla


def calcular_capitalfinal(tasamensual, meses, capital, aportemensual):
    """
    Calcula el capital final acumulado al término de un período específico.

    Args:
    - tasamensual (float): Tasa mensual en formato decimal.
    - meses (int): Número total de meses del período.
    - capital (float): Capital inicial invertido.
    - aportemensual (float): Aporte mensual constante.

    Returns:
    - capitalfinal (float): Monto total acumulado al final del período.
    """
    monto_capital = capital * math.pow(1 + tasamensual, meses)
    monto_aportes = aportemensual * ((math.pow(1 + tasamensual, meses) - 1) / tasamensual)
    capitalfinal = round(monto_capital + monto_aportes, 2)
    return capitalfinal


def calcular_ganancia(capital, aportemensual, meses, capitalfinal):
    """
    Calcula la ganancia obtenida y la inversión total realizada en un período específico.

    Args:
    - capital (float): Capital inicial invertido.
    - aportemensual (float): Aporte mensual constante.
    - meses (int): Número total de meses del período.
    - capitalfinal (float): Capital final acumulado al término del período.

    Returns:
    - ganancia (float): Diferencia entre el capital final y la inversión total realizada.
    - inversiontotal (float): Suma del capital inicial y los aportes realizados.
    """
    inversiontotal = capital + (aportemensual * meses)
    ganancia = round(capitalfinal - inversiontotal, 2)
    return ganancia, inversiontotal