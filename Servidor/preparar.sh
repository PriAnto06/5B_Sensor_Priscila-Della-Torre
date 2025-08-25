#crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate
#instalar el flask
pip install flask
#para ver la version
flask --version
#para correr
flask run --debug
#crear la base de datos
sqlite3 datos3.sqlite < base de datos.sql
#para ejecutar la base de datos
source preparar.sh
# opcion 2 .preparar.sh