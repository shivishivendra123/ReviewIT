from django.contrib import admin
from .models import Org,Org_login,Services
from .models import Admin
# Register your models here.
admin.site.register(Org)
admin.site.register(Org_login)
admin.site.register(Services)
admin.site.register(Admin)