import datetime
import json
import traceback

from decouple import config as config_environment


from sqlalchemy import func
from sqlalchemy.orm import aliased

from src.models.GsUsers import GsUsers
from src.models.GsUserObjects import GsUserObjects
from src.models.GsObjects import GsObjects
from src.database.db_mysql import Session
from src.utils.Logger import Logger

session = Session()

def integrationGPS():
    result_list = []
    try:
        # Alias para las tablas
        guo = aliased(GsUserObjects)
        usu = aliased(GsUsers)
        gso = aliased(GsObjects)

        # Subconsulta para obtener la zona horaria del usuario 'admin'
        timezone_subquery = (
            session.query(func.substr(GsUsers.timezone, 1, 3))
            .filter(GsUsers.username == config_environment('USER_QUERY'))
            .scalar()  # Obtiene el valor escalar (el valor de la subconsulta)
        ).replace(' ', '')

        with session:
            query = (
                session.query(
                    guo.imei,
                    guo.object_id,
                    gso.plate_number,
                    gso.dt_tracker,
                    gso.altitude,
                    gso.protocol,
                    gso.dt_tracker,
                    gso.dt_server,
                    gso.lat,
                    gso.lng,
                    gso.angle,
                    gso.odometer,
                    gso.params,
                    gso.speed,
                    gso.name,
                    gso.device,
                    gso.satelites
                )
                .select_from(guo)  
                .join(usu, usu.id == guo.user_id)
                .join(gso, gso.imei == guo.imei)
                .filter(usu.username == config_environment('USER_QUERY'))
                .limit(1000)
            )

            # Ejecuta la consulta
            results = query.all()

        # Convierte los resultados en una lista de diccionarios
        
        for row in results:

            textSearchTopten = 'acc'
            textSearchTeltonik = 'io239'
            ignicion = 0

            if textSearchTopten in row[12] or textSearchTeltonik in row[12]:
                try:
                    json_data = json.loads(row[12])
                    if isinstance(json_data, dict):
                        if textSearchTopten in row[12]:
                            ignicion = json_data[textSearchTopten]
                        if textSearchTeltonik in row[12]:
                            ignicion = json_data[textSearchTeltonik]
                except json.JSONDecodeError:
                    pass

            evento = 42
            if ignicion != 0 and row[13] > 0:
                evento = 41

            fechaHora = row[6] - datetime.timedelta(hours=abs(int(timezone_subquery)))

            result_dict = {

                'patente': row[2],
                'imei': row[0],
                'latitud': str(row[8]),
                'longitud': str(row[9]),
                'altitud': row[4],
                'fechaHora': fechaHora.strftime("%Y-%m-%d %H:%M:%S") if row[3] else None if row[6] else row[6],
                'evento': evento,
                'velocidad': row[13],
                'heading': row[10],
                'ignicion': ignicion
            }

            result_list.append(result_dict)
        
        return result_list


    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return result_list.append({
            'error': str(ex),
            'success': False
        })