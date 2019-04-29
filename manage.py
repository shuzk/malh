import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# from info import app, db
from info import create_app, db

# 创建app， 并传入配置模式：development / production
app = create_app('development')

# 添加数据库迁移
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    # session['name'] = 'itheima'

    logging.debug('测试debug')
    logging.warning('测试warning')
    logging.error('测试error')
    logging.fatal('测试fatal')

    return 'index'

if __name__ == '__main__':
    manager.run()
