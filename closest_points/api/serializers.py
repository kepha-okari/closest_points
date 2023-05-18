from rest_framework import serializers
from .models import Point

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['id', 'x', 'y', 'closest_point_x', 'closest_point_y']
