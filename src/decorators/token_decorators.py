import traceback

from datetime import datetime, timedelta
from decouple import config
from flask import request, jsonify
from functools import wraps
from jwt import encode, decode, ExpiredSignatureError, InvalidSignatureError

from src.utils.Logger import Logger

def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, 'exp': expire_date(int(config('EXPIRE_DATE'))) }, key=config('SECRET_KEY'), algorithm='HS256')
    return token.encode('UTF-8')

def verify_token(func):
    @wraps(func)
    def decorador(*args, **kwargs):
        secret = config('SECRET_KEY')
        try:
            encoded_token = request.headers['token']
            if ((len(encoded_token) > 0) and (encoded_token.count('.') <= 3)):
                try:
                    decode(encoded_token, secret, algorithms=["HS256"])
                    return func()
                except (ExpiredSignatureError, InvalidSignatureError):
                    response = jsonify({'message': 'Unauthorized'})
                    return response, 401
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            response = jsonify(
                {
                    'message': 'Unauthorized', 
                }
            )
            return response, 401
        except:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            response = jsonify(
                {
                    'message': 'Unauthorized', 
                }
            )
            return response, 401
    return decorador


