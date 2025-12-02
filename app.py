# app.py

from flask import Flask, render_template
# Importamos tu lógica de Python
from crono_logic_core import CronoLogicCore

# 1. Inicializar la aplicación Flask
app = Flask(__name__)
# Inicializamos tu agenda
agenda_core = CronoLogicCore()

# 2. Definir la RUTA PRINCIPAL (el index o la página de inicio)
@app.route('/')
def index():
    # Obtener los eventos ordenados y pasarlos a la plantilla HTML
    eventos = agenda_core.obtener_eventos_ordenados()
    
    # Renderizamos la plantilla 'index.html'
    # SI ESTE ARCHIVO FALTA, LA APP CRASHEA SILENCIOSAMENTE
    return render_template('index.html', eventos=eventos)

# # app.py

# ... (el resto del código sigue igual)

# 3. Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    # Usamos debug=True, el puerto 8080 y el host 0.0.0.0
    app.run(debug=True, port=8080, host='0.0.0.0')