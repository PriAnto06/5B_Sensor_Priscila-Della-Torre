from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Variable para guardar el historial en memoria (simple)
historial_alertas = []

@app.route('/api/test', methods=['GET'])
def home():
    return "API de Seguridad Activa (esp.py). Usa /api/alerta para enviar datos."

@app.route('/api/alerta', methods=['POST'])
def recibir_alerta():
    data = request.get_json()
    
    tipo = data.get('tipo', 'Desconocido')
    mensaje = data.get('mensaje', 'Sin mensaje')
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"🚨 [ALERTA RECIBIDA] {hora} | Tipo: {tipo} | Mensaje: {mensaje}")
    
    # Guardamos en el historial
    alerta = {
        "hora": hora,
        "tipo": tipo,
        "mensaje": mensaje
    }
    historial_alertas.append(alerta)
    
    return jsonify({"status": "recibido", "timestamp": hora}), 200

@app.route('/api/ver-alertas', methods=['GET'])
def ver_alertas():
    return jsonify(historial_alertas), 200

if __name__ == '__main__':
    # Ejecuta el servidor accesible en la red local
    # Puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)