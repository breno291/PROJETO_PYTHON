from app import create_app

# Cria o app e roda
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
