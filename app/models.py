from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=11)
    role_id = models.IntegerField()


class Role(models.Model):
    role_type = models.IntegerField()
    created_time = models.CharField()


class Server_list(models.Model):
    server_name = models.CharField(max_length=100)
    ip = models.CharField(max_length=200)  # 考虑是否可以使用整型存储
    administrator = models.IntegerField()
    service_type = models.CharField()  # 暂时使用字符串,日后可以考虑使用postgres的数组类型


class Action(models.Model):
    action = models.IntegerField()  # 由系统预定义
    execute_time = models.TimeField() # 定义精确的执行时间
