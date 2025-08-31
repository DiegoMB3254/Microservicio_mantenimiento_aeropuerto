from flask import Flask
from flasgger import Swagger
from simulation.MantenimientoController import mantenimiento_bp

def create_app():
    app = Flask(__name__)

    # Configurar Swagger
    app.config['SWAGGER'] = {
        'title': 'API de Mantenimientos',
        'uiversion': 3
    }
    Swagger(app)

    # Registrar Blueprint
    app.register_blueprint(mantenimiento_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return "Microservicio de Mantenimientos corriendo"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
