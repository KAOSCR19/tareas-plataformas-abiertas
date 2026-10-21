from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint 1: Mensaje de bienvenida
@app.route('/estudiantes/api/v1/hola', methods=['GET'])
def hola():
    return jsonify({
        "mensaje": "Bienvenido a la API de estudiantes"
    })

# Endpoint 2: Saludo al estudiante
@app.route('/estudiantes/api/v1/saludo', methods=['GET'])
def saludo():

    datos = request.get_json(silent=True) or {}

    nombre = datos.get('nombre', '')

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({
            "mensaje": "Debe de ingresar el nombre del estudiante."
        })

    return jsonify({
        "mensaje": "Hola " + nombre.strip()
    })


# Endpoint 3: Información del estudiante
@app.route('/estudiantes/api/v1/informacion', methods=['GET'])
def informacion():

    nombre = request.args.get('nombre', '').strip()
    carrera = request.args.get('carrera', '').strip()

    if not nombre or not carrera:
        return jsonify({
            "mensaje": "Debe ingresar el nombre y la carrera del estudiante."
        })

    return jsonify({
        "nombre": nombre,
        "carrera": carrera,
        "estado": "Activo",
        "mensaje": "Información del estudiante consultada correctamente."
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
