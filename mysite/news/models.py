from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField(max_length=None)  
    data = models.DateTimeField()
    image = models.ImageField(blank=True)

    def __unicode__(header):
        return header.header

    def get_absolute_url(self):
        return "/news/%i/" % self.id
