#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 13:50
# @Author  : wangwei
# @Site    : www.rich-f.com
# @File    : setting.py
# @Software: Rich Web Platform
# @Function: 系统-配置
import os
import datetime


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.urandom(24)
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 指定日志的格式，按照每天一个日志文件的方式
    LOG_FILE = './logs/myFlask.log'
    LOGCONFIG = {
        'version': 1,
        'disable_existing_loggers': False,

        'filters': {
            'require_debug_false': {
                '()': 'richwebsys.logging.log.RequestFilter'
            }
        },
        'formatters': {
            'simple': {
                'format': '[%(levelname)s] %(module)s : %(message)s'
            },
            'verbose': {
                'format':
                    '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': LOG_FILE,
                'maxBytes': 1024 * 1024 * 1024,
                'encoding': "utf-8",
                'backupCount': 10
            },
        },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }

    #######################################
    # ##############JWT配置############   #
    # 用户验证输入字段
    # JWT_AUTH_USER_CODE_KEY = 'user_code'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = True  # 开启token CSRF保护
    JWT_CSRF_IN_COOKIES = False  # 禁止将CSRF值设置在cookie中，用户登录时直接以JSON方式返回
    JWT_ACCESS_COOKIE_PATH = '/'  # 默认允许前端向任务后端接口发送该cookie
    JWT_REFRESH_COOKIE_PATH = '/'  # 默认允许前端向任务后端接口发送该cookie
    JWT_ACCESS_CSRF_HEADER_NAME = 'x_access_csrf_token'  # access_token对应的CSRF值对应的键名
    JWT_REFRESH_CSRF_HEADER_NAME = 'x_refresh_csrf_token'  # refresh_token请求头中的CSRF对应的键名
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=120)  # access过期时间
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)  # 过期时间


class ProdConfig(Config):
    """生产配置."""

    ENV = 'prod'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # 拦截重定向
    # # MONGODB_SETTINGS = {'db': '', 'host': '', 'port': 27017}
    # MONGODB_SETTINGS = {'db': '', 'host': '', 'port': 25000, 'username': '',
    #                     'password': ""}


class DevConfig(Config):
    """开发配置."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    DEBUG_TB_INTERCEPT_REDIRECTS = False  # 拦截重定向
    MONGODB_SETTINGS = {'': '', 'host': '', 'port': 25000, 'username': '',
                        'password': ""}
