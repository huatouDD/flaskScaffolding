from apps.flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_logconfig import LogConfig
from flask_cors import CORS

bcrypt = Bcrypt()

# db =

# 日志
logcfg = LogConfig()

# jwt
jwt = JWTManager()

# csrf跨域
cors = CORS()
