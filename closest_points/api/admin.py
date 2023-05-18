from django.contrib import admin
from .models import Point

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'x', 'y', 'closest_point_x', 'closest_point_y')
