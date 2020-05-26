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

    SECRET_KEY = os.environ.get('RICHWEBSYS_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13  # 决定encryption的复杂程度，默认值为12

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BAIDU_MAP_URL = 'https://api.map.baidu.com/geocoder/v2'  # 百度地图URL
    BAIDU_OUTPUT = '&output=json&ak=Bfy0cxLPhsblXnda2x36WRDPUuMGSfsp'  # 百度地图out_put
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
                'level': 'DEBUG',  # TODO
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'file': {
                'level': 'DEBUG',  # TODO
                'class': 'logging.FileHandler',
                'formatter': 'verbose',
                'filename': LOG_FILE,
                'mode': 'a',
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
