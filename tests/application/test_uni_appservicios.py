from django.test import TestCase
from django.urls import reverse


class ServiciosViewTest(TestCase):

    def setUp(self):
        # Cambia "servicios" por el nombre real de tu URL si es distinto
        self.url = reverse('servicios')

    def test_servicios_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'servicios.html')

    def test_titulo_presente(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Nuestros Servicios")

    def test_textos_de_servicios(self):
        response = self.client.get(self.url)

        textos = [
            "Consulta del recién nacido",
            "Enfermedades respiratorias",
            "Enfermedades de la piel",
            "Enfermedades gastrointestinales",
            "Control del niño sano",
            "Consulta para adolescentes",
            "Manejo de malnutrición",
            "Certificado de salud",
            "Nebulizaciones",
            "Evaluación inicial del desarrollo emocional"
        ]

        for texto in textos:
            self.assertContains(response, texto)

    def test_imagen_principal_existe(self):
        response = self.client.get(self.url)
        self.assertContains(response, "consulta_bebe.png")

    def test_boton_servicios_existe(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'id="btn-servicios"')
