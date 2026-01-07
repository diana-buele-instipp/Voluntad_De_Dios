import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_pagina_servicios_carga_correctamente():
    """
    Prueba de integración para la página de Servicios.
    Verifica que:
    - La URL responde con 200
    - Contiene títulos y elementos importantes
    - Carga correctamente las imágenes estáticas
    - Muestra la lista de servicios
    """

    client = Client()

    # Asegúrate de usar el nombre correcto de tu URL:
    url = reverse('servicios')   # 👉 si tu URL tiene otro name, cámbialo aquí

    response = client.get(url)

    # 1) Código correcto
    assert response.status_code == 200, "❌ La página Servicios no cargó con estado 200."

    contenido = response.content.decode()

    # 2) Elementos del encabezado
    assert "Nuestros Servicios" in contenido, "❌ No aparece el botón o título de servicios."
    assert "Voluntad De Dios" in contenido or "Voluntad de Dios" in contenido, \
        "❌ No aparece el título principal en la página."

    # 3) Verificar imágenes importantes
    assert "img/voluntad_dios.png" in contenido, "❌ Imagen del título no encontrada."
    assert "img/logo_de.png" in contenido, "❌ logo de institucional no encontrado."
    assert "img/consulta_bebe.png" in contenido, "❌ Imagen de 'consulta bebe' no cargada."

    # 4) Lista de servicios
    servicios_esperados = [
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

    for servicio in servicios_esperados:
        assert servicio in contenido, f"❌ No aparece el servicio: {servicio}"

    print("✅ Prueba de integración de SERVICIOS ejecutada correctamente.")
