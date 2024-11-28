from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#
API_BASE_URL = "https://www.googleapis.com/sql/v1beta4/projects/myProject/instances/myInstance/users"
API_KEY = "AIzaSyBCreD4pKYY_IA946XLjLZNgf2QtkQIk50"  

@app.route('/crear_receta', methods=['POST'])
def crear_receta():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        ingredientes = data.get('ingredientes')
        pasos = data.get('pasos')

        # Validar los datos
        if not nombre or not ingredientes or not pasos:
            return jsonify({"error": "Faltan datos esenciales"}), 400

        # Construir la URL con la clave API
        url = f"{API_BASE_URL}?key={API_KEY}"

        # Hacer la solicitud POST a la API REST
        response = requests.post(url, json={
            'nombre': nombre,
            'ingredientes': ingredientes,
            'pasos': pasos
        })

        # Manejar la respuesta
        if response.status_code == 201:
            return jsonify({"message": "Receta creada correctamente!"}), 201
        else:
            return jsonify({"error": f"No se pudo crear la receta en la API: {response.text}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/listar_recetas', methods=['GET'])
def listar_recetas():
    try:
        # Construir la URL con la clave API
        url = f"{API_BASE_URL}?key={API_KEY}"

        # Hacer la solicitud GET a la API REST
        response = requests.get(url)

        # Manejar la respuesta
        if response.status_code == 200:
            recetas = response.json()
            return jsonify(recetas), 200
        else:
            return jsonify({"error": f"No se pudieron obtener las recetas: {response.text}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
