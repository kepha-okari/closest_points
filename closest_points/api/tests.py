from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class ClosestPointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_closest_points_valid_input(self):
        points_data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post('/api/closest_points/', data=points_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('closest_points', response.data)
        self.assertIn('record', response.data)
        # Add assertions to check the correctness of the closest_points and record in the response

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
