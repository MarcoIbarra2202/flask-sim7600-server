from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Página principal (confirmación de que el servidor está activo)
@app.route('/')
def index():
    return "Servidor Flask activo ✅"

# Endpoint para recibir datos del SIM7600
@app.route('/datos', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON vacío o formato inválido"}), 400

        # Guardar los datos en un archivo dentro del servidor
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"{fecha} - {data}\n"
        with open("datos_recibidos.txt", "a") as f:
            f.write(linea)

        print(f"📩 Dato recibido: {data}")
        return jsonify({"status": "ok", "received": data}), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

