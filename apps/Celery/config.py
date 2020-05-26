

BROKER_URL = 'redis://xxxxx:6379/12'
CELERY_RESULT_BACKEND = 'redis://xxxxxx:6379/13'

# 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 启动时区设置
CELERY_ENABLE_UTC = True

# 在5s内完成，不然杀死worker, 任务移交父进程
CELERY_TASK_TIME_LIMIT = 8

# 并发worker数量
CELERYD_CONCURRENCY = 18

# 单个任务的运行时间限制，否则会被杀死
CELERYD_TASK_TIME_LIMIT = 10

CELERY_FORCE_EXECV = True # 非常重要, 防止死锁

CELERY_DISABLE_RATE_LIMITS = True

CELERY_LOG_FORMAT = "[%(asctime)s:%(levelname)s%(processName)s%(message)s]"