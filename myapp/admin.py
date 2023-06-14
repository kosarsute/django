from django.contrib import admin

from .models import Logger
from .models import Booking
from .models import Employees

admin.site.register(Logger)
admin.site.register(Booking)
admin.site.register(Employees)
