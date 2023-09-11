## configuración skynav-integration-python

1. instalar dependencias con el comnado:

```pip instal requirements.txt```

Eso instalara las siguientes dependencias:

```
bcrypt==4.0.1
blinker==1.6.2
click==8.1.7
colorama==0.4.6
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
flask-swagger==0.2.14
flask-swagger-ui==4.11.1
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
psycopg2-binary==2.9.7
PyJWT==2.8.0
PyMySQL==1.1.0
python-decouple==3.8
python-dotenv==1.0.0
PyYAML==6.0.1
SQLAlchemy==2.0.20
typing_extensions==4.7.1
Werkzeug==2.3.7
```

2. Crear el archivo .env dentro de la raiz del proyecto.

```sudo nano .env```

dentro del archivo se debe agregar los siguiente:

```
HOST_API = 'https://host_donde_el_servidor'
HOST = 'ip_host'
USER = ''
PASSWORD = ''
PORT = N° de puerto
DB = ''
USER_QUERY = 'usuario con el que se ejcutara'
LOG_DIRECTORY = ''
ENVIRONMENTS = "desarrollo|produccion"
SECRET_KEY = ""
EXPIRE_DATE = ""
```
