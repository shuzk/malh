from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import app, db

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
