from django.apps import apps
from django.test import TestCase
from .apps import ToDoConfig


class TestToDoConfig(TestCase):

    def test_app(self):
        self.assertEqual("to_do", ToDoConfig.name)
        self.assertEqual("to_do", apps.get_app_config("to_do").name)