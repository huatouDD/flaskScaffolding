from flask import Flask

from apps.auth.auths import user_loader_handler
from apps.extensions import bcrypt, logcfg, cors, jwt
from apps.settings import ProdConfig


def create_app(config_object=ProdConfig):
    app = Flask(__name__)

    # 导入settings
    app.config.from_object(config_object)

    # 扩展文件
    register_extensions(app)
    # 蓝图
    register_blueprint(app)


def register_extensions(app):
    pass


def register_blueprint(app):
    bcrypt.init_app(app)
    logcfg.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    jwt.user_loader_callback_loader(user_loader_handler)   # 加载当前用户处理的对象函数
