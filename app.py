from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Carpeta donde se guardarán los datos
if not os.path.exists("data"):
    os.makedirs("data")

@app.route('/')
def home():
    return "Servidor Flask activo ✅"

@app.route('/datos', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json()
        print(f"📦 Datos recibidos: {data}")

        # Guardar en archivo (uno por día)
        fecha = datetime.now().strftime("%Y-%m-%d")
        with open(f"data/{fecha}.txt", "a") as f:
            f.write(str(data) + "\n")

        return jsonify({"status": "ok", "msg": "Datos recibidos correctamente"}), 200
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
