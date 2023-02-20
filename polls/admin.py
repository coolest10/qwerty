from django.contrib import admin

from .models import Izdelie

admin.site.register(Izdelie)

from .models import Detal

admin.site.register(Detal)
