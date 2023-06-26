from django.contrib import admin

# Register your models here.
from .models import TblApoderado ,TblParentesco

admin.site.register(TblApoderado)
admin.site.register(TblParentesco)