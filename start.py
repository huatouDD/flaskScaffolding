from celery import Celery
from flask.helpers import get_debug_flag

from apps import create_app
from apps.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig
app = create_app(CONFIG)

celery = Celery(app.name)
celery.config_from_object('apps.Celery.config')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)
