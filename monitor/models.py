from django.db import models


class DBinfo(models.Model):
    db_type = models.CharField(max_length=100)
    # create_at = models.DateTimeField('create time')


class Host(models.Model):
    hostname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    ip = models.IntegerField(default=0)
