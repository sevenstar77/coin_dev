# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.urls import reverse
# from django.test import TestCase
# import unittest
#
# # Create your tests here.
# # class UnitTest(unittest.TestCase):
# #     def test(self):
# #
# #         self.assertEqual(1, 2)
#
# class ScheduleTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_emailschedules_list(self):
#         #response = self.client.get('/api/v1.0/schedules/emailschedules/')
#         response = self.client.get(reverse('schedules:emailschedules'))
#         print(response)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)