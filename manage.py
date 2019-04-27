from flask import Flask

app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True


app.config.from_object(Config)
