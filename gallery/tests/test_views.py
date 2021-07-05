import unittest
from django.test import TestCase, Client
from django.http import Http404
from django.urls import reverse

from .. import views
class TestViews(TestCase):
    def setUp(self):
        client = Client()
        self.list_url = reverse('photo_list')

    def test_photo_list_GET(self):

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'photo_list.html')






