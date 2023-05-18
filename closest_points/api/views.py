# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.request import Request
from .models import Point
from .serializers import PointSerializer



@api_view(['POST'])
def closest_points(request):
    # Parse the points from the request data
    points_str = request.data.get('points')
    if not points_str:
        return Response({'error': 'No points provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        points = [tuple(map(int, p.split(','))) for p in points_str.split(';')]
        
        # Find the closest points
        closest_points = find_closest_points(points)

        # Create Point objects and store them in the database
        record = save_points_to_database(points, closest_points)

        # Return the closest points
        closest_points_str = ';'.join([','.join(map(str, p)) for p in closest_points])
        return Response({'closest_points': closest_points_str}, status=status.HTTP_201_CREATED)

    except ValueError:
        return Response({'error': 'Invalid points format'}, status=status.HTTP_400_BAD_REQUEST)

   


def find_closest_points(points):
    closest_points = []
    min_distance = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if distance < min_distance:
                min_distance = distance
                closest_points = [points[i], points[j]]
    return closest_points


def save_points_to_database(points, closest_points):
    for p in points:
        closest_point = closest_points[0] if (p != closest_points[1] and p != closest_points[0]) else closest_points[1]
        point = Point.objects.create(x=p[0], y=p[1], closest_point_x=closest_point[0], closest_point_y=closest_point[1])
        point.save()

