from django.contrib import admin
from .models import Customer , Provider , User
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Provider)