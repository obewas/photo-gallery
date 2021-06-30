from django.test import TestCase
from ..models import Category

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.name = Category.objects.create(name=Category.Travel)
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))

    def tearDown(self):
        self.name.dispose()