from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from catalog.models import Link


class LinkViewSetTestCase(APITestCase):
    def setUp(self):
        # Create objects
        self.link = Link.objects.create(
            title="link title",
            description="link description",
            icon="fa fa-link",
            url="http://oraculodev.com",
        )
        Link.objects.create(title="link title 2", description="link description 2")

        # Get urls
        self.list_url = reverse("link-list")
        self.detail_url = reverse("link-detail", args=(self.link.pk,))

    def test_link_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_link_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.link.title)
        self.assertEqual(response.data["description"], self.link.description)
        self.assertEqual(response.data["icon"], self.link.icon)
        self.assertEqual(response.data["url"], self.link.url)

    def test_link_create_not_allowed(self):
        response = self.client.post(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_pin_delete_not_allowed(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_pin_update_not_allowed(self):
        response = self.client.put(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_pin_partial_update_not_allowed(self):
        response = self.client.patch(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
