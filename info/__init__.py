import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config

# app = Flask(__name__)
# # 加载配置
# app.config.from_object(Config["development"])
#
# # 初始化数据库
# db = SQLAlchemy(app)
# # 初始化reids存储对象
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# # 开启csrf保护
# CSRFProtect(app)
# # 设置session保存指定位置
# Session(app)

db = SQLAlchemy()
redis_store = None

def create_app(config_name):
    """通过传入不同的配置，，"""

    app = Flask(__name__)

    # 配置
    app.config.from_object(config[config_name])
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    return app

