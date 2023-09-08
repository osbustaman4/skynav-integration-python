from sqlalchemy import Column, String, Integer, Boolean
from src.database.db_mysql import Base

class GsUserObjects(Base):
    __tablename__ = 'gs_user_objects'

    object_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    imei = Column(String(20))
    group_id = Column(Integer)
    driver_id = Column(Integer)
    trailer_id = Column(Integer)
    velocidad_alerta = Column(String(5))
    alerta_enviada = Column(Boolean, nullable=False)
    
    def __init__(
            self,
            object_id,
            user_id,
            imei,
            group_id,
            driver_id,
            trailer_id,
            velocidad_alerta,
            alerta_enviada,
    ):
        self.object_id = object_id
        self.user_id = user_id
        self.imei = imei
        self.group_id = group_id
        self.driver_id = driver_id
        self.trailer_id = trailer_id
        self.velocidad_alerta = velocidad_alerta
        self.alerta_enviada = alerta_enviada