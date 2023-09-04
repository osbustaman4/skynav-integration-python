from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from src.routes import BaseRvmRoutes

from decouple import config as config_environment


app = Flask(__name__)

if config_environment('ENVIRONMENTS') == "desarrollo":
    # swagger configs
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'


else:
    SWAGGER_URL = '/'
    API_URL = ''


SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Todo Lista Endpoints"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(BaseRvmRoutes.main_login, url_prefix='/login')
    app.register_blueprint(BaseRvmRoutes.main_getPatentInformation, url_prefix='/get-patent-information')
    return app