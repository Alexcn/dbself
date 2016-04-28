from django.db import models


class DBinfo(models.Model):
    hostname = models.CharField(max_length=200)
    db_type = models.CharField(max_length=10)


class Host(models.Model):
    hostname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    ip = models.IntegerField()
