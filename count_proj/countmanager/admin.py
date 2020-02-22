from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header= 'Boston Code Camp Attendace Manager'

admin.site.register(Room)
admin.site.register(Speaker)
admin.site.register(Session)
admin.site.register(TimeSlot)