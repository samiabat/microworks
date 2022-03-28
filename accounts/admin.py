from django.contrib import admin

# Register your models here.

from .models import *

# admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Proposal)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(Report)