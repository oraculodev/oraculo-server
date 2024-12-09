from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models.component import Component


class ComponentModelTest(TestCase):
    def setUp(self):
        self.component = Component.objects.create(name="Beecambio API", repo_id=103093)

    def test_create(self):
        self.assertTrue(Component.objects.exists())

    def test_name_blank_and_null(self):
        field = Component._meta.get_field("name")
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_str(self):
        self.assertEqual("Beecambio API", str(self.component))
