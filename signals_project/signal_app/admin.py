from django.contrib import admin
from .models import YourModel,Rectangle
@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name',)  


@admin.register(Rectangle)
class RectangleAdmin(admin.ModelAdmin):
    list_display = ('length', 'width')