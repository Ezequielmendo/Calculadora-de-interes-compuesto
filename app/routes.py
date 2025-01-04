from flask import request, render_template, redirect, flash, url_for
from app import app

from app.funciones import calcular_capitalfinal, calcular_ganancia, generar_tabla

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Capturar datos del formulario
            capital = float(request.form['capitalinicial'])
            tasainteres = float(request.form['tasa'])
            periodo = int(request.form['periodo'])
            aportemensual = float(request.form['aportemensual'])

            # Cálculos principales
            tasamensual = tasainteres / 100 / 12  # Convertir tasa anual a mensual en decimal
            meses = periodo * 12  # Convertir periodo en años a meses

            # Calcular el monto final usando interés compuesto
            capitalfinal = calcular_capitalfinal(tasamensual, meses, capital, aportemensual)

            # Calcular ganancia y total invertido
            ganancia, inversiontotal = calcular_ganancia(capital, aportemensual, meses, capitalfinal)

            # Generar datos para la tabla de resultados
            datos_tabla = generar_tabla(periodo, capital, tasamensual, aportemensual)

            # Renderizar resultados
            return render_template(
                'index.html',
                capitalfinal=capitalfinal,
                ganancia=ganancia,
                inversiontotal=inversiontotal,
                datos_tabla=datos_tabla
            )
        except Exception:
            flash('Error al realizar los cálculos. Por favor, revisa los datos ingresados.', 'error')
            return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('index.html', capitalfinal=None)