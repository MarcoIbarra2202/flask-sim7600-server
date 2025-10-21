from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor Flask activo ✅"

@app.route('/datos', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json(force=True)
        print(f"📩 Dato recibido: {data}")  # Esto aparecerá en los logs de Render
        return jsonify({"received": data, "status": "ok"}), 200
    except Exception as e:
        print(f"⚠️ Error al procesar datos: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
