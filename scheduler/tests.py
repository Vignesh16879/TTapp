from django.test import TestCase
from .models import teacher, student 


class TestCase(TestCase):
    def setUp(self):
        teacher.objects.create(name='TestObject', description='This is a test object.')
        student.objects.create(name='TestObject', description='This is a test object.')

    def test_model_data(self):
        # Get the object from the database
        test_object1 = teacher.objects.get(name='TestObject')
        test_object2 = student.objects.get(name='TestObject')
        
        # Perform your assertions
        self.assertEqual(test_object1.name, 'TestObject')
        self.assertEqual(test_object1.description, 'This is a test object.')
        self.assertEqual(test_object2.name, 'TestObject')
        self.assertEqual(test_object2.description, 'This is a test object.')