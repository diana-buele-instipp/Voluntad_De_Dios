from django.test import TestCase
from django.urls import reverse


class BaseTemplateIntegrationTest(TestCase):

    def test_base_template_status_code(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_base_contains_header(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, "Consultorio Voluntad de Dios")

    def test_base_contains_navigation_links(self):
        response = self.client.get(reverse('inicio'))

        self.assertContains(response, "Inicio")
        self.assertContains(response, "Servicios")
        self.assertContains(response, "Información")

    def test_base_contains_phone(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, "0988605465")

    def test_base_uses_base_template(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, "base.html")
