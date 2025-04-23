from flask import Blueprint, render_template, jsonify
from app import db

main = Blueprint('main', __name__)

# Rota para a página inicial
@main.route('/')
def index():
    return render_template('index.html')

# Rota de teste do banco
@main.route('/test-db')
def test_db():
    try:
        conn = db.session.execute('SELECT 1')
        return jsonify(message="Banco conectado com sucesso!")
    except Exception as e:
        return jsonify(message=f"Erro ao conectar no banco: {str(e)}"), 500
