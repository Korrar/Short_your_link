from django.db import models
from url.validators import validate_link

class Links(models.Model):
    link_id = models.AutoField(primary_key=True)
    url_link = models.CharField(max_length=512, validators=[validate_link])
    url_shorted_link = models.CharField(max_length=512)

class Shortcut(models.Model):
    shortcut = models.CharField(primary_key=True, max_length=6)
