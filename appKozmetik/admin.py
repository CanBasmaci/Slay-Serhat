from django.contrib import admin
from .models import *

from .models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(Profil)

