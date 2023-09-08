from app_config import configure
from src import init_app
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from src.utils.Cron import Cron

configuration = configure['development']
app = init_app(configuration)

# Agregar esta línea para definir la variable 'application'
application = app


task_001 = BackgroundScheduler()
task_001.add_job(Cron.task_IntegrationGPS, 'interval', seconds=10)  # Reemplaza N con la cantidad de segundos deseados
task_001.start()

if __name__ == '__main__':
    load_dotenv()
    app.run(host='0.0.0.0', port=5000)