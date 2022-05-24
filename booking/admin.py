from django.contrib import admin
from .models import Mybooking, Branch, Teller, Shift
# Register your models here.
admin.site.register(Mybooking)
admin.site.register(Branch)
admin.site.register(Teller)
admin.site.register(Shift)