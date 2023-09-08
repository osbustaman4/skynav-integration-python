from sqlalchemy import Column, String, Integer, TIMESTAMP, Date, DateTime, Float, Boolean
from src.database.db_mysql import Base

class GsObjects(Base):
    __tablename__ = 'gs_objects'

    imei = Column(String(20), primary_key=True)
    protocol = Column(String(50))
    net_protocol = Column(String(3))
    ip = Column(String(50))
    port = Column(String(10))
    active = Column(String(5))
    object_expire = Column(String(5))
    object_expire_dt = Column(Date)
    manager_id = Column(Integer)
    dt_server = Column(DateTime)
    dt_tracker = Column(DateTime)
    lat = Column(Float)
    lng = Column(Float)
    altitude = Column(Float)
    angle = Column(Float)
    speed = Column(Float)
    loc_valid = Column(Integer)
    params = Column(String(2048))
    dt_last_stop = Column(DateTime)
    dt_last_idle = Column(DateTime)
    dt_last_move = Column(DateTime)
    name = Column(String(50))
    icon = Column(String(256))
    map_arrows = Column(String(512))
    map_icon = Column(String(5))
    tail_color = Column(String(7))
    tail_points = Column(Integer)
    device = Column(String(30))
    sim_number = Column(String(50))
    model = Column(String(60))
    vin = Column(String(50))
    plate_number = Column(String(50))
    odometer_type = Column(String(10))
    engine_hours_type = Column(String(10))
    odometer = Column(Float)
    engine_hours = Column(Integer)
    fcr = Column(String(512))
    time_adj = Column(String(30))
    accuracy = Column(String(1024))
    dt_chat = Column(DateTime)
    overpass = Column(Boolean, nullable=False)
    run_speed = Column(Boolean, nullable=False)
    corte_motor = Column(Integer, nullable=False)
    comando_corte = Column(String(30))
    robado = Column(Integer)
    satelites = Column(Integer)
    rele_activo = Column(Boolean, nullable=False)
    max_speed = Column(Integer)
    dt_robo = Column(TIMESTAMP, nullable=False)


    def __init__(
            self,
            imei,
            protocol,
            net_protocol,
            ip,
            port,
            active,
            object_expire,
            object_expire_dt,
            manager_id,
            dt_server,
            dt_tracker,
            lat,
            lng,
            altitude,
            angle,
            speed,
            loc_valid,
            params,
            dt_last_stop,
            dt_last_idle,
            dt_last_move,
            name,
            icon,
            map_arrows,
            map_icon,
            tail_color,
            tail_points,
            device,
            sim_number,
            model,
            vin,
            plate_number,
            odometer_type,
            engine_hours_type,
            odometer,
            engine_hours,
            fcr,
            time_adj,
            accuracy,
            dt_chat,
            overpass,
            run_speed,
            corte_motor,
            comando_corte,
            robado,
            satelites,
            rele_activo,
            max_speed,
            dt_robo
    ):
        self.imei = imei
        self.protocol = protocol
        self.net_protocol = net_protocol
        self.ip = ip
        self.port = port
        self.active = active
        self.object_expire = object_expire
        self.object_expire_dt = object_expire_dt
        self.manager_id = manager_id
        self.dt_server = dt_server
        self.dt_tracker = dt_tracker
        self.lat = lat
        self.lng = lng
        self.altitude = altitude
        self.angle = angle
        self.speed = speed
        self.loc_valid = loc_valid
        self.params = params
        self.dt_last_stop = dt_last_stop
        self.dt_last_idle = dt_last_idle
        self.dt_last_move = dt_last_move
        self.name = name
        self.icon = icon
        self.map_arrows = map_arrows
        self.map_icon = map_icon
        self.tail_color = tail_color
        self.tail_points = tail_points
        self.device = device
        self.sim_number = sim_number
        self.model = model
        self.vin = vin
        self.plate_number = plate_number
        self.odometer_type = odometer_type
        self.engine_hours_type = engine_hours_type
        self.odometer = odometer
        self.engine_hours = engine_hours
        self.fcr = fcr
        self.time_adj = time_adj
        self.accuracy = accuracy
        self.dt_chat = dt_chat
        self.overpass = overpass
        self.run_speed = run_speed
        self.corte_motor = corte_motor
        self.comando_corte = comando_corte
        self.robado = robado
        self.satelites = satelites
        self.rele_activo = rele_activo
        self.max_speed = max_speed
        self.dt_robo = dt_robo


        
    