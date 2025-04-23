from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

# Instanciando o banco de dados e o MySQL
db = SQLAlchemy()
mysql = MySQL()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializando as extensões
    db.init_app(app)
    mysql.init_app(app)

    # Importar as rotas (você vai criar o routes.py em breve)
    from app.routes import main
    app.register_blueprint(main)

    return app
