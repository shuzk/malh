import redis
from flask import Flask
from flask import session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import Config


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
