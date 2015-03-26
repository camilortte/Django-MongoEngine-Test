# -*- coding: utf-8 -*-

from django.db import models  
from djangotoolbox.fields import DictField


class Article(models.Model):  
    title = models.CharField(max_length=64)  
    content = models.TextField()  
    cosa = DictField()

    def __unicode__(self):
        return u"Objecto"
