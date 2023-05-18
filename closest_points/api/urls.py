from django.urls import path
from .views import closest_points

urlpatterns = [
    path('closest_points/', closest_points, name='closest_points'),
    # path('api/view_points/', view_points, name='view_points'),
]
