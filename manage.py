import redis
from flask import Flask
from flask import session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand




class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/malhflasksql"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化reids存储对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

# 添加数据库迁移
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    # session['name'] = 'itheima'
    return 'index'

if __name__ == '__main__':
    manager.run()
