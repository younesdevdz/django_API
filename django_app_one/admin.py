from django.contrib import admin

from .models import Reporting , Breakdown , Intervention

admin.site.register(Breakdown)
admin.site.register(Reporting)
admin.site.register(Intervention)
