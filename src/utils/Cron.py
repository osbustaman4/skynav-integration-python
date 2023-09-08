import json
import requests
import traceback

from src.utils.Logger import Logger

from src.Integrations.QuerysIntegrations import integrationGPS

class Cron():

    @classmethod
    def task_IntegrationGPS(self):
        
        payload = json.dumps(integrationGPS())
        url = "https://external.skynav.cl/integrador/centinela/test/transmision"
        headers = {
            'Authorization': 'Bearer 2881d9c2d0db7d7422db8f8d5e935aedb6c359dad59e239f1fc8c7e6c43404b02451fe7b651910a95926a564755f8eac308bc3e7cad88a38851eced3c86a88af',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != 200:
            Logger.add_to_log_cron("success", str(response.text))
            Logger.add_to_log_cron("success", traceback.format_exc())
        else:
            Logger.add_to_log("error", str(response.text))
            Logger.add_to_log("error", traceback.format_exc())

        print(f"{response.status_code}")
        print(f"{response.text}")
        print(" ********************** ")

    
    