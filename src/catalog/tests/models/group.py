from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Group


class GroupModelTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="dream group")

    def test_create(self):
        self.assertTrue(Group.objects.exists())

    def test_name_blank_and_null(self):
        field = Group._meta.get_field("name")
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_str(self):
        self.assertEqual("dream group", str(self.group))
