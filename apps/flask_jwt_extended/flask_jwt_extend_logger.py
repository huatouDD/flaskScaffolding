"""
针对jwt的日志
"""

import logging

# 获取logger对象，如不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象
import os
from logging.handlers import RotatingFileHandler

jwt_logger = logging.getLogger(__name__)
# 设置等级
jwt_logger.setLevel(logging.DEBUG)
# 创建日志文件路径
log_dir_name = "logs"
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
logger_file_name = log_file_path + os.sep + 'flask-jwt.log'
# 创建文件日志记录器，指定日志保存的路径，每个日志文件的最大值，最后保存的日志文件数量
file_log_handler = RotatingFileHandler(
    filename=logger_file_name,
    maxBytes=1024*1024*1024,
    backupCount=10,
    encoding="UTF-8"
)

# 创建日志记录格式，记录时间/等级名/记录消息
# 发起日志调用的源文件的完整路径名以及调用所在的源文件行的行号
file_handler_formatter = logging.Formatter(
    '%(asctime)s %(levelname): %(message)s [in %(pathname)s:%(lineno)d]'
)

# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(file_handler_formatter)
# 设置handler的处理等级
file_log_handler.setLevel(logging.DEBUG)
# 为flask-jwt的logger对象添加日志路记录器
jwt_logger.addHandler(file_log_handler)