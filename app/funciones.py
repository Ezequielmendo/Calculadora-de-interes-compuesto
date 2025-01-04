import math


def calcular_tasa_mensual_y_meses(tasainteres, periodo):
    tasamensual = tasainteres / 100 / 12  # Convertir tasa anual a mensual en decimal
    meses = periodo * 12  # Convertir periodo en años a meses
    return tasamensual, meses


def generar_tabla(periodo, capital, tasamensual, aportemensual):
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
    monto_capital = capital * math.pow(1 + tasamensual, meses)
    monto_aportes = aportemensual * ((math.pow(1 + tasamensual, meses) - 1) / tasamensual)
    capitalfinal = round(monto_capital + monto_aportes, 2)
    return capitalfinal


def calcular_ganancia(capital, aportemensual, meses, capitalfinal):
    inversiontotal = capital + (aportemensual * meses)
    ganancia = round(capitalfinal - inversiontotal, 2)
    return ganancia, inversiontotal