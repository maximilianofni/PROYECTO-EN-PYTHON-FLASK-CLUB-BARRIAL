from flask import Flask

def create_app():
    app = Flask(__name__)
    
#ruta de prueba
    @app.route("/")
    def home():
         return "hola mundo"  