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
    def setUp(cls):
        cls.location = 'Kisumu'
        cls.location = Location.objects.create(name=cls.location)
        cls.category = 'Family'
        cls.category = Category.objects.create(name=cls.category)
        cls.image = Image.objects.create(label='Best', image="shoes.jpg",description='test',
        category=cls.category, location=cls.location, year_taken='2012-02-12')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))