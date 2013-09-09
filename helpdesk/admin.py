from django.contrib import admin
from helpdesk.models import *

admin.site.register(Incident)
admin.site.register(ServiceCategory)
admin.site.register(IncidentLocation)
admin.site.register(Category)