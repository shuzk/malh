# import logging
#
# from manage import app
from . import index_blu


@index_blu.route("/")
def index():
    return "index"


# @app.route('/')
# def index():
#     # session['name'] = 'itheima'
#
#     logging.debug('测试debug')
#     logging.warning('测试warning')
#     logging.error('测试error')
#     logging.fatal('测试fatal')
#
#     return 'index'
