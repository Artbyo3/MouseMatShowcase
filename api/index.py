from app import create_app
import os

# Crear la aplicación Flask
app = create_app()

# Configurar para Vercel
if __name__ == '__main__':
    app.run(debug=True)
