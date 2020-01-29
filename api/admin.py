from django.contrib import admin
from .models import Api_message, Api_user, UV

# Register your models here.
admin.site.register(Api_message)
admin.site.register(Api_user)
admin.site.register(UV)