from flask import Flask,g, jsonify, request, url_for
from math import ceil
import sqlite3
def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}

def abrirConexion():
   if 'db' not in g:
      g.db = sqlite3.connect("datos3.sqlite")
      g.db.row_factory = dict_factory
   return g.db
def cerrarConexion(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

app = Flask(__name__)
app.teardown_appcontext(cerrarConexion)

@app.route("/api/test")
def test():
    return "funcionando!"

#@app.route("/")
#def hello_world():
 #   return "<p>Hello, World!</p>"

#json
#{
   # "nombre":"luxometro",
    #"valor": "135"
#}

@app.route("/api/sensor",methods=["POST"])
def sensor():
    servidor = request.json
    nombre = servidor['nombre']
    valor = servidor['valor']
    print(f"Nombre: {nombre} - Valor: {valor}")
    db = abrirConexion()
    db.execute("INSERT INTO ESP32(Nombre,Valor) VALUES(?,?)", (nombre,valor))
    db.commit()
    datos = { "resultado": "Ok",
             "nombre": nombre,
             "valor": valor }
    cerrarConexion()
    return datos

@app.route("/api/sensor/datos",methods=["GET"])
def obtener_datos():
   db = abrirConexion()
   cursor = db.execute("SELECT * FROM ESP32")
   datos = cursor.fetchall()
   cerrarConexion()
   return {
      "resultado": "Ok",
      "datos": datos
   }