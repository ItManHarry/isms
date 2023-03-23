from django.db import models
from django.contrib.auth.models import User
from db import BaseModel
class SysLoginLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(BaseModel.Meta):
        db_table = 'sys_login_log'