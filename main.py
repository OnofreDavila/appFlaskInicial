from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        promedio: float = (nota1 + nota2 + nota3) / 3
        asistencia = float(request.form['asistencia'])
        resultado = ''
        if nota1 > 10 and nota1 < 70 and nota2 > 10 and nota2 < 70 and nota3 > 10 and nota3 < 70 and asistencia >= 75 and asistencia < 100:
            if promedio >= 40:
                resultado = 'APROBADO'
            else:
                resultado = 'NO APROBADO'
            return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
        elif asistencia < 75:
            resultado = 'NO APROBADO POR FALTA DE ASISTENCIA'
            return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
        elif asistencia > 100:
            resultado = 'NO es posible tener una asistencia mayor del 100%'
            return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
        return render_template('ejercicio1.html')
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        long_nombre1 = len(nombre1)
        long_nombre2 = len(nombre2)
        long_nombre3 = len(nombre3)

        #procedo a comparar las longitudes de cada nombre mediante un if-else
        if long_nombre1 > long_nombre2 and long_nombre1 > long_nombre3:
            resultado = nombre1
            longitud = long_nombre1
        elif long_nombre2 > long_nombre1 and long_nombre2 > long_nombre3:
            resultado = nombre2
            longitud = long_nombre2
        elif long_nombre3 > long_nombre1 and long_nombre3 > long_nombre2:
            resultado = nombre3
            longitud = long_nombre3
        else:
            resultado = 'las longitudes son iguales o hay empate.'
        return render_template('ejercicio2.html',resultado=resultado, longitud=longitud)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)