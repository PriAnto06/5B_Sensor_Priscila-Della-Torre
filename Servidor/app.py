from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#json
#{
   # "nombre":"luxometro",
    #"valor": "135"
#}

@app.route("/api/sensor",methods=["POST"])
def sensor():
    servidor = request.json
    nombre = servidor.get["luxometro"]
    valor = servidor.get ["135"]
    print(f"Nombre: {servidor['nombre']} - Valor: {servidor['valor']}")
    return "OK"