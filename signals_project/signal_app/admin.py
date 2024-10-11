from django.contrib import admin
from .models import sig,Rectangle
@admin.register(sig)
class sigAdmin(admin.ModelAdmin):
    list_display = ('name',)  


@admin.register(Rectangle)
class RectangleAdmin(admin.ModelAdmin):
    list_display = ('length', 'width')