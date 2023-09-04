import logging
import os
import traceback
import subprocess
import platform

from decouple import config as config_environment


class Logger():

    def __set_logger(self):
        log_directory = config_environment('LOG_DIRECTORY')
        log_filename = 'app.log'

        # Obtener el nombre del sistema operativo
        operating_system = platform.system()
        if operating_system == "Linux":
            # Comando para cambiar los permisos
            chmod_command = f"sudo chmod -R u+rwx {log_directory}"

            # Ejecutar el comando en la terminal
            subprocess.run(chmod_command, shell=True)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(self, level, message):
        try:
            logger = self.__set_logger(self)

            if (level == "critical"):
                logger.critical(message)
            elif (level == "debug"):
                logger.debug(message)
            elif (level == "error"):
                logger.error(message)
            elif (level == "info"):
                logger.info(message)
            elif (level == "warn"):
                logger.warn(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)