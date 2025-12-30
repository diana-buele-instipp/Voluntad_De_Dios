import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_informacion_content():
    client = Client()

    url = reverse("informacion")
    response = client.get(url)

    assert response.status_code == 200

    contenido = response.content.decode()

    # Título principal
    assert "UBICACIÓN" in contenido

    # Dirección
    assert "Machala San Martín Entre Buenavista y Séptima Este" in contenido

    # Nombre de la doctora
    assert "Echeverría Loayza Domenica Lilibeth" in contenido

    # Horarios
    assert "Lunes a Viernes" in contenido
    assert "08am a 08pm" in contenido
    assert "Sábado" in contenido
    assert "08am a 04pm" in contenido

    # Imagen doctora
    assert "img/doctora.png" in contenido

    # Mapa de Google
    assert "google.com/maps" in contenido
