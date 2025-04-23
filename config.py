import os

class Config:
    # Configuração do MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@localhost/banco_teste'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita o tracking de modificações (evita avisos)
    SECRET_KEY = os.urandom(24)  # Chave secreta para sessões
