from sqlalchemy import Column, String, Integer, Boolean, Date, Text, DateTime, Float
from src.database.db_mysql import Base

class GsUsers(Base):
    __tablename__ = 'gs_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(String(5))
    account_expire = Column(String(5))
    account_expire_dt = Column(Date)
    privileges = Column(Text)
    manager_id = Column(Integer)
    manager_billing = Column(String(5))
    username = Column(String(100))
    password = Column(String(100))
    sess_hash = Column(String(100))
    email = Column(String(100))
    api = Column(String(5))
    api_key = Column(String(100))
    dt_reg = Column(DateTime)
    dt_login = Column(DateTime)
    ip = Column(String(100))
    notify_account_expire = Column(String(5))
    notify_object_expire = Column(String(5))
    info = Column(String(1024))
    comment = Column(String(2048))
    obj_add = Column(String(5))
    obj_limit = Column(String(5))
    obj_limit_num = Column(Integer)
    obj_days = Column(String(5))
    obj_days_dt = Column(Date)
    obj_edit = Column(String(5))
    obj_history_clear = Column(String(5))
    currency = Column(String(3))
    timezone = Column(String(30))
    dst = Column(String(5))
    dst_start = Column(String(20))
    dst_end = Column(String(20))
    language = Column(String(20))
    units = Column(String(6))
    map_sp = Column(String(7))
    map_is = Column(Float)
    map_rc = Column(String(7))
    map_rhc = Column(String(7))
    groups_collapsed = Column(String(100))
    od = Column(String(10))
    ohc = Column(String(256))
    chat_notify = Column(String(40))
    sms_gateway_server = Column(String(5))
    sms_gateway = Column(String(5))
    sms_gateway_type = Column(String(5))
    sms_gateway_url = Column(String(2048))
    sms_gateway_identifier = Column(String(20))
    places_markers = Column(String(4))
    places_routes = Column(String(4))
    places_zones = Column(String(4))
    usage_email_daily = Column(String(4))
    usage_sms_daily = Column(String(8))
    usage_api_daily = Column(String(8))
    usage_email_daily_cnt = Column(Integer)
    usage_sms_daily_cnt = Column(Integer)
    usage_api_daily_cnt = Column(Integer)
    dt_usage_d = Column(Date)
    overpass = Column(Boolean, nullable=False)
    history_import = Column(Boolean, nullable=False)
    rut = Column(String(45))
    sesion = Column(Integer)
    privilegios = Column(String(255))
    cartecF = Column(Integer, nullable=False)
    pass_verificada = Column(Boolean, nullable=False)


    def __init__(
        self,
        active,
        account_expire,
        account_expire_dt,
        privileges,
        manager_id,
        manager_billing,
        username,
        password,
        sess_hash,
        email,
        api,
        api_key,
        dt_reg,
        dt_login,
        ip,
        notify_account_expire,
        notify_object_expire,
        info,
        comment,
        obj_add,
        obj_limit,
        obj_limit_num,
        obj_days,
        obj_days_dt,
        obj_edit,
        obj_history_clear,
        currency,
        timezone,
        dst,
        dst_start,
        dst_end,
        language,
        units,
        map_sp,
        map_is,
        map_rc,
        map_rhc,
        groups_collapsed,
        od,
        ohc,
        chat_notify,
        sms_gateway_server,
        sms_gateway,
        sms_gateway_type,
        sms_gateway_url,
        sms_gateway_identifier,
        places_markers,
        places_routes,
        places_zones,
        usage_email_daily,
        usage_sms_daily,
        usage_api_daily,
        usage_email_daily_cnt,
        usage_sms_daily_cnt,
        usage_api_daily_cnt,
        dt_usage_d,
        overpass,
        history_import,
        rut,
        sesion,
        privilegios,
        cartecF,
        pass_verificada
    ):
        self.active = active
        self.account_expire = account_expire
        self.account_expire_dt = account_expire_dt
        self.privileges = privileges
        self.manager_id = manager_id
        self.manager_billing = manager_billing
        self.username = username
        self.password = password
        self.sess_hash = sess_hash
        self.email = email
        self.api = api
        self.api_key = api_key
        self.dt_reg = dt_reg
        self.dt_login = dt_login
        self.ip = ip
        self.notify_account_expire = notify_account_expire
        self.notify_object_expire = notify_object_expire
        self.info = info
        self.comment = comment
        self.obj_add = obj_add
        self.obj_limit = obj_limit
        self.obj_limit_num = obj_limit_num
        self.obj_days = obj_days
        self.obj_days_dt = obj_days_dt
        self.obj_edit = obj_edit
        self.obj_history_clear = obj_history_clear
        self.currency = currency
        self.timezone = timezone
        self.dst = dst
        self.dst_start = dst_start
        self.dst_end = dst_end
        self.language = language
        self.units = units
        self.map_sp = map_sp
        self.map_is = map_is
        self.map_rc = map_rc
        self.map_rhc = map_rhc
        self.groups_collapsed = groups_collapsed
        self.od = od
        self.ohc = ohc
        self.chat_notify = chat_notify
        self.sms_gateway_server = sms_gateway_server
        self.sms_gateway = sms_gateway
        self.sms_gateway_type = sms_gateway_type
        self.sms_gateway_url = sms_gateway_url
        self.sms_gateway_identifier = sms_gateway_identifier
        self.places_markers = places_markers
        self.places_routes = places_routes
        self.places_zones = places_zones
        self.usage_email_daily = usage_email_daily
        self.usage_sms_daily = usage_sms_daily
        self.usage_api_daily = usage_api_daily
        self.usage_email_daily_cnt = usage_email_daily_cnt
        self.usage_sms_daily_cnt = usage_sms_daily_cnt
        self.usage_api_daily_cnt = usage_api_daily_cnt
        self.dt_usage_d = dt_usage_d
        self.overpass = overpass
        self.history_import = history_import
        self.rut = rut
        self.sesion = sesion
        self.privilegios = privilegios
        self.cartecF = cartecF
        self.pass_verificada = pass_verificada
