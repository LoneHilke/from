from django.contrib import admin
from .models import Playground
from .models import Tags
from .models import Store

# Register your models here.
admin.site.register(Playground)
admin.site.register(Tags)
admin.site.register(Store)