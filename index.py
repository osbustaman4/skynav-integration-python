from app_config import configure
from src import init_app
from dotenv import load_dotenv

configuration = configure['development']
app = init_app(configuration)

# Agregar esta línea para definir la variable 'application'
application = app

if __name__ == '__main__':
    load_dotenv()
    app.run(host='0.0.0.0', port=5000)