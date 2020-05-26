

def create_app(config_object=ProdConfig):
    app = FLask(__name__)

    # 导入settings
    app.config.from_object(config_object)


    # 扩展文件
    register_extensions(app)
    # 蓝图
    register_blueprint(app)


def register_extensions(app):
    pass


def register_blueprint(app):
    pass
