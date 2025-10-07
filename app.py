from flask import Flask
from flasgger import Swagger
from simulation.MantenimientoController import mantenimiento_bp
from database.session import Base, engine
from persistence.entity.MantenimientoEntity import MantenimientoEntity

def create_app():
    app = Flask(__name__)

    # Configurar Swagger
    app.config['SWAGGER'] = {
        'title': 'API de Mantenimientos',
        'uiversion': 3
    }
    Swagger(app)

    # Crear tablas si no existen
    with app.app_context():
        Base.metadata.create_all(bind=engine)

    # Registrar Blueprint
    app.register_blueprint(mantenimiento_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return "Microservicio de Mantenimientos corriendo"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
