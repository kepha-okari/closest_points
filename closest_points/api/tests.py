from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point
from .views import *



class ClosestPointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_closest_points_valid_input(self):
        points_data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post('/api/closest_points/', data=points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('closest_points', response.data)
        # Add assertions to check the correctness of the closest_points in the response

    def test_closest_points_missing_points(self):
        response = self.client.post('/api/closest_points/', data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'No points provided')

    def test_closest_points_empty_points(self):
        points_data = {'points': ''}
        response = self.client.post('/api/closest_points/', data=points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        # Add assertions to check the correctness of the error message in the response

    def test_closest_points_invalid_points_format(self):
        points_data = {'points': '2,2;-1,30;20,11;4,5;'}
        response = self.client.post('/api/closest_points/', data=points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        #Add assertions to check the correctness of the error message in the response

    def test_find_closest_points_two_points(self):
        points = [(1, 1), (2, 2)]
        expected_result = [(1, 1), (2, 2)]
        result = find_closest_points(points)
        self.assertEqual(result, expected_result)

    def test_find_closest_points_three_points(self):
        points = [(1, 1), (2, 2), (3, 3)]
        expected_result = [(1, 1), (2, 2)]
        result = find_closest_points(points)
        self.assertEqual(result, expected_result)

    def test_find_closest_points_multiple_points(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        expected_result = [(1, 1), (2, 2)]
        result = find_closest_points(points)
        self.assertEqual(result, expected_result)

    def test_closest_points_invalid_input_size(self):
        points_data = {'points': '2,2;4,5'}
        response = self.client.post('/api/closest_points/', data=points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid size of input')
   
    def test_save_points_to_database(self):
        points = [(2, 2), (-1, 30), (20, 11), (4, 5)]
        closest_points = [(2, 2), (4, 5)]

        # Save the points to the database
        save_points_to_database(points, closest_points)

        # Verify that the last added point is saved in the database
        saved_point = Point.objects.latest('id')
        self.assertEqual(saved_point.x, points[-1][0])
        self.assertEqual(saved_point.y, points[-1][1])

        # Check the closest point coordinates
        closest_point = closest_points[0] if (saved_point.x != closest_points[1][0] and saved_point.y != closest_points[1][1]) else closest_points[1]
        self.assertEqual(saved_point.closest_point_x, closest_point[0])
        self.assertEqual(saved_point.closest_point_y, closest_point[1])
