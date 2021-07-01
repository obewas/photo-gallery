from django.test import TestCase
from ..models import Category, Image, Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Family')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image.objects.create(label='Best', image="shoes.jpg",description='test',
        category=Category.name, location=Location.name, year_taken='2012-02-12')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))