from functools import wraps
from sys_sign.models import SysLoginLog
'''
    写入日志
'''
def log_record(request, content):
    def decorator(function):
        @wraps(function)
        def decorated_function(*args, **kwargs):
            if request.user:
                log = SysLoginLog()
                log.save()
            else:
                print('User has not login...')
            return function(*args, **kwargs)
        return decorated_function
    return decorator