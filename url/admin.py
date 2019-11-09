from django.contrib import admin
from django.apps import apps
from url.models import Links,Shortcut


admin.site.register(Links)
admin.site.register(Shortcut)