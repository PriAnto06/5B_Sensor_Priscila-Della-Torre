from flask import Flask,g, jsonify, request, url_for
from math import ceil
import sqlite3

resultados_por_pag = 3
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
   args = request.args
   pagina = int(args.get('page', '1'))
   descartar = (pagina-1)* resultados_por_pag
   db = abrirConexion()
   cursor =db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM ESP32;")
   cant = cursor.fetchone()['cant']
   paginas= ceil(cant / resultados_por_pag)

   if pagina < 1 or pagina > paginas:
       return f"Página inexistente: {pagina}", 400
   
   cursor.execute("""SELECT Nombre, Valor
                      FROM ESP32
                      LIMIT ? OFFSET ?;""",
                   (resultados_por_pag, descartar))
   lista = cursor.fetchall()
   cerrarConexion(db)
   siguiente = None
   anterior = None
   if pagina > 1:
       anterior = url_for('obtener_datos', page=pagina-1, _external=True)
   if pagina < paginas:
       siguiente = url_for('obtener_datos', page=pagina+1, _external=True)
   info = { 'count' : cant, 'pages': paginas,
             'next' : siguiente, 'prev' : anterior }
   res = { 'info' : info, 'results' : lista}
   return jsonify(res)







#def obtener_datos():
   #db = abrirConexion()
   #cursor = db.execute("SELECT * FROM ESP32")
   #datos = cursor.fetchall()
   #cerrarConexion()
   #return {
     # "resultado": "Ok",
     # "datos": datos
   #}