from django.test import TestCase

from .models import Menu
# Create your tests here.

class MenuModelTest(TestCase): 
    @classmethod
    def setUpTestData(cls): 
        cls.menu = Menu.objects.create(
            name = 'Sergei',
            price = 100
        )
    def test_fields(self): 
        self.assertIsInstance(self.menu.name, str)

        self.assertIsInstance(self.menu.price, int)
