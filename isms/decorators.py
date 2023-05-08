from functools import wraps
from sys_sign.models import SysLoginLog
from django.contrib.auth.models import User
'''
    写入日志
'''
def log_record(content):
    def decorator(function):
        @wraps(function)
        def decorated_function(*args, **kwargs):
            user = User.objects.get(pk=1)
            log = SysLoginLog(user=user, content=content)
            log.save()
            return function(*args, **kwargs)
        return decorated_function
    return decorator