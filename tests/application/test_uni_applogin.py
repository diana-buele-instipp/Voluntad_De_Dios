import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_login_page_loads_correctly():
    client = Client()

    # Debe existir una URL con name="login"
    url = reverse("login")
    response = client.get(url)

    assert response.status_code == 200

    contenido = response.content.decode()

    # Título principal
    assert "Voluntad de Dios" in contenido

    # Texto clave del contenido
    assert "La consulta incluye" in contenido

    # Botones visibles
    assert "Consulta" in contenido
    assert "Consulta Online" in contenido

    # Elementos del menú
    assert "Inicio" in contenido
    assert "Servicios" in contenido
    assert "Información" in contenido

    # Imagen principal / doctora
    assert "doctora.png" in contenido or "doctora" in contenido
