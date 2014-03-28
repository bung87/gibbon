# -*- coding: utf-8 -*-
from django.db import models

class Event(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    showtime = models.DateTimeField()
    showname = models.CharField(max_length=16)
    state = models.IntegerField()